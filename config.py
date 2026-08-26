from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from libs.config.api import HTTPClientSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
        extra="ignore",
    )

    api: HTTPClientSettings


@lru_cache
def get_settings() -> Settings:
    return Settings()
