from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    title: str = ''

    class Config:
        env_file = '../.env'


settings = Settings()
