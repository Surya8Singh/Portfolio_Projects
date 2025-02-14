from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List
import os
from dotenv import load_dotenv
from .constants import *

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    # Base Settings
    ENV: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = DEBUG
    API_V1_PREFIX: str = API_V1_PREFIX
    PROJECT_NAME: str = PROJECT_NAME
    
    # API Settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME", DEFAULT_MODEL_NAME)
    
    # CORS Settings
    ALLOWED_ORIGINS: List[str] = ALLOWED_ORIGINS
    
    # Database Settings (for future use)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Vector Store Settings
    VECTOR_STORE_PATH: str = os.getenv("VECTOR_DB_PATH", VECTOR_STORE_DIR)
    CHUNK_SIZE: int = CHUNK_SIZE
    CHUNK_OVERLAP: int = CHUNK_OVERLAP
    
    # Model Settings
    TEMPERATURE: float = DEFAULT_TEMPERATURE
    MAX_TOKENS: int = MAX_TOKENS

    class Config:
        case_sensitive = True
        env_file = ".env"

# Cache the settings instance
@lru_cache()
def get_settings() -> Settings:
    return Settings()

# Create settings instance
settings = get_settings()