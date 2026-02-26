from fastapi.testclient import TestClient
from fastapi import status

def test_read_attribute(client: TestClient):
    client.post(
        "/attribute/",
        json={
            "title": "Color",
        },
    )

    response = client.get("/attribute/?limit=1")
    data = response.json()

    assert data["count"] == 1      
    assert len(data["data"]) == 1

    result = data["data"][0]

    assert isinstance(result["id"], int)
    assert result["title"] == "Color"

def test_read_attribute_by_id(client: TestClient):
    create_response = client.post(
        "/attribute/",
        json={
            "title": "Color",
        },
    )
    attribute_id = create_response.json()["id"]

    response = client.get(f"/attribute/{attribute_id}")
    
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result["id"] == attribute_id
    assert result["title"] == "Color"

def test_create_attribute(client: TestClient):
    response = client.post(
        "/attribute/",
        json={
            "title": "Color",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["title"] == "Color"

def test_update_attribute(client: TestClient):
    create_response = client.post(
        "/attribute/",
        json={
            "title": "Color",
        },
    )
    attribute_id = create_response.json()["id"]

    response = client.patch(
        f"/attribute/{attribute_id}",
        json={
            "title": "Color 2",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert isinstance(result["id"], int)
    assert result["title"] == "Color 2"

def test_delete_attribute(client: TestClient):
    create_response = client.post(
        "/attribute/",
        json={
            "title": "Color",
        },
    )
    attribute_id = create_response.json()["id"]

    response = client.delete(f"/attribute/{attribute_id}")
    assert response.status_code == status.HTTP_200_OK