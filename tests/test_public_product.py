from fastapi.testclient import TestClient
from fastapi import status

def test_read_products(client: TestClient):
    client.post(
        "/product/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
    )

    response = client.get("/public-product/?limit=1")
    data = response.json()
    
    assert data["count"] == 1      
    assert len(data["data"]) == 1

    result = data["data"][0]

    assert isinstance(result["id"], int)
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"

def test_read_product_by_id(client: TestClient):
    create_response = client.post(
        "/product/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
    )
    product_id = create_response.json()["id"]

    response = client.get(f"/public-product/{product_id}")
    
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result["id"] == product_id
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"