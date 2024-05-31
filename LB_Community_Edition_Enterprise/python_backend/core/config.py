import collections
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the backend API. They are automatically read from environment variables. If not found, they use a
    default value. There are also validators to check the format of fields.
    """
    api_v1_str: str = '/api/v1'
    secret_key: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    access_token_expire_minutes: int = 60 * 24 * 8
    example_school: str = '994'
    server_name: str = ''
    server_host: AnyHttpUrl = 'http://localhost'
    backend_cors_origins: List[AnyHttpUrl] = ['http://localhost:8000', 'http://localhost', 'http://localhost:4200',
                                              'http://localhost:3000', 'http://localhost:8080', 'http://localhost:5173']
    postgres_server: str = ""
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_db: str = ""
    project_name: str = ""
    sqlalchemy_database_uri: Optional[PostgresDsn] = None
    sentry_dsn: Optional[HttpUrl] = None
    smtp_tls: bool = True
    smtp_port: Optional[int] = None
    smtp_host: Optional[str] = None
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    emails_from_email: Optional[EmailStr] = None
    emails_from_name: Optional[str] = None
    email_reset_token_expire_hours: int = 48
    email_templates_dir: str = "email-templates/build"
    emails_enabled: bool = False
    email_test_user: EmailStr = "test@example.com"
    first_superuser: EmailStr = "test@example.com"
    first_superuser_password: str = ""
    users_open_registration: bool = False

    @field_validator("backend_cors_origins")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @field_validator("sentry_dsn")
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if isinstance(v, collections.abc.Sized):
            if len(v) == 0:
                return None
            return v
        return None

    @field_validator("sqlalchemy_database_uri")
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("postgres_user"),
            password=values.data.get("postgres_password"),
            host=values.data.get("postgres_server") or "localhost",
            path=values.data.get('postgres_db')
        )

    @field_validator("emails_from_name")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values.data.get("project_name")
        return v

    @field_validator("emails_enabled")
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.data.get("smtp_host")
            and values.data.get("smtp_port")
            and values.data.get("emails_from_email")
        )

    class Config:
        case_sensitive = True


settings = Settings()
