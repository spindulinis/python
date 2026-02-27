from fastapi.testclient import TestClient
from fastapi import status

def test_read_category(client: TestClient, admin_token_headers: dict):
    client.post(
        "/category/",
        json={
            "order": 10,
            "title": "Fruit",
            "description": "Fruit category",
        },
        headers=admin_token_headers
    )

    response = client.get("/category/?limit=1", headers=admin_token_headers)
    data = response.json()

    assert data["count"] == 1      
    assert len(data["data"]) == 1

    result = data["data"][0]

    assert isinstance(result["id"], int)
    assert result["order"] == 10
    assert result["title"] == "Fruit"
    assert result["description"] == "Fruit category"

def test_read_category_by_id(client: TestClient, admin_token_headers: dict):
    create_response = client.post(
        "/category/",
        json={
            "order": 10,
            "title": "Fruit",
            "description": "Fruit category",
        },
        headers=admin_token_headers
    )
    category_id = create_response.json()["id"]

    response = client.get(f"/category/{category_id}", headers=admin_token_headers)
    
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result["id"] == category_id
    assert result["order"] == 10
    assert result["title"] == "Fruit"
    assert result["description"] == "Fruit category"

def test_create_category(client: TestClient, admin_token_headers: dict):
    response = client.post(
        "/category/",
        json={
            "order": 10,
            "title": "Fruit",
            "description": "Fruit category",
        },
        headers=admin_token_headers
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["order"] == 10
    assert result["title"] == "Fruit"
    assert result["description"] == "Fruit category"

def test_update_category(client: TestClient, admin_token_headers: dict):
    create_response = client.post(
        "/category/",
        json={
            "order": 10,
            "title": "Fruit",
            "description": "Fruit category",
        },
        headers=admin_token_headers
    )
    category_id = create_response.json()["id"]

    response = client.patch(
        f"/category/{category_id}",
        json={
            "order": 102,
            "title": "Fruit 2",
            "description": "Fruit category 2",
        },
        headers=admin_token_headers
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["order"] == 102
    assert result["title"] == "Fruit 2"
    assert result["description"] == "Fruit category 2"

def test_delete_category(client: TestClient, admin_token_headers: dict):
    create_response = client.post(
        "/category/",
        json={
            "order": 10,
            "title": "Fruit",
            "description": "Fruit category",
        },
        headers=admin_token_headers
    )
    category_id = create_response.json()["id"]

    response = client.delete(f"/category/{category_id}", headers=admin_token_headers)
    assert response.status_code == status.HTTP_200_OK