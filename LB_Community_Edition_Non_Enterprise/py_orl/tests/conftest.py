from typing import Generator

import pytest
from fastapi.testclient import TestClient

import app
from db.session import SessionLocal


@pytest.fixture(scope="session")
def db() -> Generator:
    """
    Database test fixture.
    """
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """
    API client test fixture.
    """
    with TestClient(app) as c:
        yield c

# @pytest.fixture(scope="module")
# def superuser_token_headers(client: TestClient) -> Dict[str, str]:
#     """
#     Unused, but keeping for documentation.
#     """
#     return get_superuser_token_headers(client)
#
#
# @pytest.fixture(scope="module")
# def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
#     """
#     Unused, but keeping for documentation.
#     """
#     return authentication_token_from_email(
#         client=client, email=settings.email_test_user, db=db
#     )
