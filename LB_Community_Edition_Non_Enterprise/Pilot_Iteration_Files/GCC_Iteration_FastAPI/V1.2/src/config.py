from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str  # Load from an environment variable

    model_config = SettingsConfigDict(
        env_file=".env",  # Load environment variables from this file
        extra="ignore"
    )

settings = Settings()

print(settings.model_dump())  # Dump the settings to check their values
