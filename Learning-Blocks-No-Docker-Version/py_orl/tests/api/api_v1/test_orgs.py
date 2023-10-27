from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from core.config import settings
from tests.utils.org import create_random_org


def test_create_org(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    """
    Test creating an org.
    """
    data = {"name": "Test School", "sourceId": "99999999"}
    response = client.post(
        f"{settings.api_v1_str}/orgs/",
        headers=superuser_token_headers,
        json=data
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["sourceId"] == data["sourceId"]
    assert "id" in content


def test_read_org(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    """
    Test reading an org.
    """
    org = create_random_org(db)
    response = client.get(
        f"{settings.api_v1_str}/orgs/{org.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == org.name
    assert content["sourceId"] == org.sourceId
    assert content["id"] == org.id
