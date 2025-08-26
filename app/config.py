from pydantic import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):
    # --- General settings ---
    PROJECT_NAME: str = "StoryGen"
    ENVIRONMENT: str = "development"  # or "production", "testing"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"

    # --- Model / ML settings ---
    MODEL_PATH: str = os.path.join("data", "models", "story_model.pt")
    TOKENIZER_PATH: str = os.path.join("data", "tokenizer")
    MAX_TOKENS: int = 256
    TEMPERATURE: float = 0.7

    # --- Server settings ---
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # --- Logging ---
    LOG_LEVEL: str = "info"  # could be "debug", "warning", "error"

    class Config:
        env_file = ".env"         # .env dosyasından da okuyabilir
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """
    Uygulama boyunca aynı Settings nesnesini cache’leyerek performans kazanır.
    """
    return Settings()