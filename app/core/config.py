from pydantic import field_validator
from pydantic_settings import BaseSettings
from typing import Any

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    DATABASE_URL: str

    @field_validator("DATABASE_URL")
    def validate_database_url(cls, v: str) -> str:
        if not v:
            raise ValueError("Database URL is required")
        return v

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
print("Settings loaded:")
print(f"API_V1_STR: {settings.API_V1_STR}")
print(f"PROJECT_NAME: {settings.PROJECT_NAME}")