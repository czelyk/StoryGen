from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Story Maker"
    version: str = "1.0.0"
    model_name: str = "mosaicml/mpt-7b-storywriter"
    max_length: int = 500
    temperature: float = 0.8
    top_k: int = 50
    top_p: float = 0.95
    device: str = None  # Otomatik algılama yapılabilir

    class Config:
        env_file = ".env"

settings = Settings()
