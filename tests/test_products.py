from fastapi.testclient import TestClient
from fastapi import status

def test_read_products(client: TestClient):
    client.post(
        "/products/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
    )

    response = client.get("/products/?limit=1")
    data = response.json()
    
    assert data["count"] == 1      
    assert len(data["data"]) == 1

    result = data["data"][0]

    assert isinstance(result["id"], int)
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"

def test_read_product_by_id(client: TestClient):
    create_response = client.post(
        "/products/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
    )
    product_id = create_response.json()["id"]

    response = client.get(f"/products/{product_id}")
    
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result["id"] == product_id
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"

def test_create_product(client: TestClient):
    response = client.post(
        "/products/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"

def test_update_product(client: TestClient):
    create_response = client.post(
        "/products/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
    )
    product_id = create_response.json()["id"]

    response = client.patch(
        f"/products/{product_id}",
        json={
            "title": "Star Wars 2",
            "description": "Movie about space wars 2",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["title"] == "Star Wars 2"
    assert result["description"] == "Movie about space wars 2"

def test_delete_product(client: TestClient):
    create_response = client.post(
        "/products/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
    )
    product_id = create_response.json()["id"]

    response = client.delete(f"/products/{product_id}")
    assert response.status_code == status.HTTP_200_OK