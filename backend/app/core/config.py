from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib import parse

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    secret_key: str
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
    )

settings = Settings()    # type: ignore[call-arg]