# backend/tests/test_vector_store.py
import pytest
import os
import shutil
from app.core.vector_store import VectorStore
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def vector_store():
    """Create a vector store instance for testing"""
    # Ensure clean test environment
    test_path = "./vector_storage"
    if os.path.exists(test_path):
        shutil.rmtree(test_path)
    
    store = VectorStore()
    yield store
    
    # Cleanup after test
    if os.path.exists(test_path):
        shutil.rmtree(test_path)

def test_vector_store_initialization(vector_store):
    """Test vector store initialization"""
    sample_texts = [
        "Python is a programming language",
        "OpenAI develops large language models",
        "Vector stores help with similarity search"
    ]
    vector_store.initialize_store(sample_texts)
    assert vector_store.vector_store is not None

def test_similarity_search(vector_store):
    """Test similarity search functionality"""
    sample_texts = [
        "Python is a programming language",
        "OpenAI develops large language models",
        "Vector stores help with similarity search"
    ]
    vector_store.initialize_store(sample_texts)
    results = vector_store.similarity_search("What is Python?", k=1)
    assert len(results) == 1
    assert "Python" in results[0].page_content

def test_add_texts(vector_store):
    """Test adding new texts"""
    initial_text = ["Initial document about programming"]
    vector_store.initialize_store(initial_text)
    
    new_text = ["Python is a versatile language"]
    vector_store.add_texts(new_text)
    
    results = vector_store.similarity_search("programming language", k=2)
    assert len(results) == 2