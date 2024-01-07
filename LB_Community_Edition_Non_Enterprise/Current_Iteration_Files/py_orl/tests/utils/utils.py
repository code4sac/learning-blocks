import random
import string
from typing import Dict

from fastapi.testclient import TestClient

from core.config import settings


def random_lower_string() -> str:
    """
    Generate a lowercase string of 32 characters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_source_id() -> int:
    """
    Generate a random source ID.
    """
    return random.randint(a=1, b=9999)


def random_email() -> str:
    """
    Generate a random email.
    """
    return f"{random_lower_string()}@{random_lower_string()}.com"


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    """
    Unused, keeping for documentation.
    """
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
