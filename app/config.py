import logging
import os
from typing import Any

from dotenv import load_dotenv
from pydantic import (
    AnyHttpUrl,
    PostgresDsn,
    ValidationInfo,
    field_validator,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Geo-City API"
    DEBUG: bool = True
    LOGGING_LEVEL: int = logging.INFO
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] | str = []

    BASE_DIR: str = os.path.dirname(os.path.dirname(__file__))

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: PostgresDsn | None = None

    API_TOKEN: str

    @field_validator("DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=info.data.get("POSTGRES_USER"),
            password=info.data.get("POSTGRES_PASSWORD"),
            host=info.data.get("POSTGRES_SERVER"),
            path=f"{info.data.get('POSTGRES_DB') or ''}",
        )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra='ignore')


settings = Settings()
