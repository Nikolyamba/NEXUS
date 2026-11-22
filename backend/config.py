from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


env_dir = Path(__file__).resolve().parent.parent / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_dir,
        env_file_encoding="utf-8"
    )

    host: str
    port: int

settings = Settings()
