from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Navora"
    app_env: str = "development"
    debug: bool = True

    database_url: str = Field(
        default="mysql+pymysql://Navora:Navora@2026%23SIH@127.0.0.1:3306/Navora",
        alias="DATABASE_URL",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
