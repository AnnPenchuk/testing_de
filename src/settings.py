from pydantic import BaseSettings, Field


class Settings_DATABASE(BaseSettings):
    user: str=Field(env='USER')
    password: str = Field(env='PASSWORD')
    host: str= Field(env='HOST')
    port: int = Field(env='PORT')
    name_database: str = Field(env='NAME_DATABASE')

class Settings_API(BaseSettings):
    url: str = Field(env='URL')


class Settings(BaseSettings):
    db=Settings_DATABASE()
    api=Settings_API()


settings = Settings()

