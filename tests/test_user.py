from fastapi.testclient import TestClient
from fastapi import status

def test_read_users(client: TestClient, admin_token_headers: dict):
    client.post(
        "/user/",
        json={
            "email": "john@doe.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
        },
        headers=admin_token_headers
    )

    response = client.get("/user/?limit=1", headers=admin_token_headers)
    data = response.json()
    
    assert data["count"] == 2      
    assert len(data["data"]) == 1

    result = data["data"][0]

    assert isinstance(result["id"], int)
    assert result["email"] == "john@doe.com"
    assert result["first_name"] == "John"
    assert result["last_name"] == "Doe"

def test_read_user_by_id(client: TestClient, admin_token_headers: dict):
    create_response = client.post(
        "/user/",
        json={
            "email": "john@doe.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
        },
        headers=admin_token_headers
    )
    user_id = create_response.json()["id"]

    response = client.get(f"/user/{user_id}", headers=admin_token_headers)
    
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result["id"] == user_id
    assert result["email"] == "john@doe.com"
    assert result["first_name"] == "John"
    assert result["last_name"] == "Doe"

def test_create_user(client: TestClient, admin_token_headers: dict):
    response = client.post(
        "/user/",
        json={
            "email": "john@doe.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
        },
        headers=admin_token_headers
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["email"] == "john@doe.com"
    assert result["first_name"] == "John"
    assert result["last_name"] == "Doe"

def test_update_user(client: TestClient, admin_token_headers: dict):
    create_response = client.post(
        "/user/",
        json={
            "email": "john@doe.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
        },
        headers=admin_token_headers
    )
    user_id = create_response.json()["id"]

    response = client.patch(
        f"/user/{user_id}",
        json={
            "email": "john@doe.com",
            "password": "password123",
            "first_name": "John2",
            "last_name": "Doe2",
        },
        headers=admin_token_headers
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["email"] == "john@doe.com"
    assert result["first_name"] == "John2"
    assert result["last_name"] == "Doe2"

def test_delete_user(client: TestClient, admin_token_headers: dict):
    create_response = client.post(
        "/user/",
        json={
            "email": "john@doe.com",
            "password": "password123",
            "first_name": "Delete",
            "last_name": "Me",
        },
        headers=admin_token_headers
    )
    user_id = create_response.json()["id"]

    response = client.delete(f"/user/{user_id}", headers=admin_token_headers)
    assert response.status_code == status.HTTP_200_OK