from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Load DATABASE_URL from .env"""

    DATABASE_URL: str
    ALEMBIC_DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
