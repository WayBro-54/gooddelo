from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    title: str = ''
    # database_url: str = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}' # noqa
    database_url: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/godello' # noqa

    class Config:
        env_file = '../.env'


settings = Settings()
