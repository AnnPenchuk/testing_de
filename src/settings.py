from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    user: str = Field(env='USER')
    password: str = Field(env='PASSWORD')
    host: str = Field(env='HOST')
    port: int = Field(env='PORT')
    db_name: str = Field(env='DB_NAME')

    class Config:
        env_file = 'C:/Users/annap/PycharmProjects/testing_de/.env.dev'


settings = Settings()

