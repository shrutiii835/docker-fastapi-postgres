from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_ignore_empty=True)

    # Project settings
    PROJECT_NAME: str = 'Docker FastAPI Postgres'
    VERSION: str = '1.0.0'
    API_V1_STR: str = '/api/v1'

    # Database settings
    POSTGRES_SERVER: str = 'db'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_DB: str = 'app'
    POSTGRES_PORT: int = 5432

    # Construct database URL
    @property
    def DATABASE_URL(self) -> str:
        return f'postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

settings = Settings()
