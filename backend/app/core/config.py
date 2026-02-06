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
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    algorithm: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
    )

    @property
    def database_url(self):
        return f"postgresql://{self.db_user}:{parse.quote(self.db_password)}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()    # type: ignore[call-arg]