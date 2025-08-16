from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATE_FORMAT: str
    LOG_FORMAT: str

    LOG_LEVEL: int

    DB_ECHO: bool

    TG_TOKEN: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://' \
               f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/' \
               f'{self.POSTGRES_DB}'

    class Config:
        env_file = '.env'


settings = Settings()
