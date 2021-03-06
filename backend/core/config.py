import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "jobboard"
    PROJECT_VERSION: str = "0.0.1"

    DATABASE_USER: str = os.getenv("POSTGRES_USER", "postgres")
    DATABASE_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "pass")
    DATABASE_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    DATABASE_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    DATABASE_DB: str = os.getenv("POSTGRES_DB", "db_course")
    DATABASE_URL: str = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    TEST_USER_EMAIL = "test@example.com"


settings = Settings()