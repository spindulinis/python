from fastapi.testclient import TestClient
from fastapi import status

def test_read_users(client: TestClient):
    for i in range(3):
        client.post("/api/v1/users/", json={
            "first_name": "John",
            "last_name": "Doe",
            "email": f"email{i}@example.com", 
            "password": "password123"
        })

    response = client.get("/api/v1/users/?limit=1")
    data = response.json()
    
    assert data["count"] == 3      
    assert len(data["data"]) == 1

def test_create_user_flow(client: TestClient):
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "tester@example.com",
            "password": "supersecretpassword",
            "first_name": "John",
            "last_name": "Doe"
        },
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "tester@example.com"
    
    # Step 2: Verify we can't create the same email twice
    duplicate_response = client.post(
        "/api/v1/users/",
        json={
            "email": "tester@example.com",
            "password": "differentpassword",
        },
    )
    assert duplicate_response.status_code == status.HTTP_400_BAD_REQUEST