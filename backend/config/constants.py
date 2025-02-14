# API Settings
API_V1_PREFIX = "/api/v1"
PROJECT_NAME = "Student Assistant Chatbot"
DEBUG = True

# CORS Settings
ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React frontend
    "http://localhost:8000",  # FastAPI backend
]

# Security Settings
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"

# Vector Store Settings
VECTOR_STORE_DIR = "vector_storage"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Model Settings
DEFAULT_MODEL_NAME = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.7
MAX_TOKENS = 2000