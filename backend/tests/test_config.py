import pytest
from app.core.config import get_validated_settings
from config.settings import Settings

def test_settings_validation():
    settings = get_validated_settings()
    assert isinstance(settings, Settings)
    assert settings.ENV in ["development", "testing", "production"]
    assert settings.MODEL_NAME is not None
    assert settings.VECTOR_STORE_PATH is not None

def test_openai_api_key():
    settings = get_validated_settings()
    assert settings.OPENAI_API_KEY is not None, "OPENAI_API_KEY must be set"