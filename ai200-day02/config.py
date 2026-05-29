from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="ai200-day02-api", alias="APP_NAME")
    app_env: str = Field(default="local", alias="APP_ENV")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    fake_model_endpoint: str = Field(
        default="https://example.invalid/model",
        alias="FAKE_MODEL_ENDPOINT",
    )
    request_timeout_seconds: int = Field(default=10, alias="REQUEST_TIMEOUT_SECONDS")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    def public_view(self) -> dict[str, str | int]:
        return {
            "app_name": self.app_name,
            "app_env": self.app_env,
            "log_level": self.log_level,
            "fake_model_endpoint": self.fake_model_endpoint,
            "request_timeout_seconds": self.request_timeout_seconds,
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()

