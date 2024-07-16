from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("../.env.dev", "../.env.secret"),
        env_file_encoding="utf-8",
    )

    host: str
    db_name: str
    user: str
    password: str
    port: int
    url: str


settings = Settings()
