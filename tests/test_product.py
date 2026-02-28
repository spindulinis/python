from fastapi.testclient import TestClient
from fastapi import status

def test_read_products(client: TestClient, admin_token_headers: dict[str, str]):
    client.post(
        "/product/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
        headers=admin_token_headers
    )

    response = client.get("/product/?limit=1", headers=admin_token_headers)
    data = response.json()
    
    assert data["count"] == 1      
    assert len(data["data"]) == 1

    result = data["data"][0]

    assert isinstance(result["id"], int)
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"

def test_read_product_by_id(client: TestClient, admin_token_headers: dict[str, str]):
    create_response = client.post(
        "/product/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
        headers=admin_token_headers
    )
    product_id = create_response.json()["id"]

    response = client.get(f"/product/{product_id}", headers=admin_token_headers)
    
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result["id"] == product_id
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"

def test_create_product(client: TestClient, admin_token_headers: dict[str, str]):
    response = client.post(
        "/product/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
        headers=admin_token_headers
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["title"] == "Star Wars"
    assert result["description"] == "Movie about space wars"

def test_update_product(client: TestClient, admin_token_headers: dict[str, str]):
    create_response = client.post(
        "/product/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
        headers=admin_token_headers
    )
    product_id = create_response.json()["id"]

    response = client.patch(
        f"/product/{product_id}",
        json={
            "title": "Star Wars 2",
            "description": "Movie about space wars 2",
        },
        headers=admin_token_headers
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["title"] == "Star Wars 2"
    assert result["description"] == "Movie about space wars 2"

def test_delete_product(client: TestClient, admin_token_headers: dict[str, str]):
    create_response = client.post(
        "/product/",
        json={
            "title": "Star Wars",
            "description": "Movie about space wars",
        },
        headers=admin_token_headers
    )
    product_id = create_response.json()["id"]

    response = client.delete(f"/product/{product_id}", headers=admin_token_headers)
    assert response.status_code == status.HTTP_200_OK