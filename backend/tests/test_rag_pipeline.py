import pytest
import os
import shutil
from pathlib import Path
from app.core.rag_pipeline import RAGPipeline

@pytest.fixture(scope="function")
def temp_dir(tmp_path):
    """Create a temporary directory for the test"""
    test_dir = tmp_path / "test_chroma_db"
    test_dir.mkdir()
    return str(test_dir)

@pytest.fixture(scope="function")
def pipeline(temp_dir):
    """Create a pipeline instance with a temporary directory"""
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set")
    
    # Create pipeline instance with temp directory
    pipe = RAGPipeline(persist_directory=temp_dir)
    
    yield pipe
    
    # Cleanup after test
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

def test_initialization(pipeline, temp_dir):
    assert pipeline.llm is not None
    assert pipeline.document_processor is not None
    assert pipeline.embeddings is not None
    assert os.path.exists(temp_dir)

def test_ingest_documents(pipeline):
    texts = [
        "Python is a programming language.",
        "LangChain is a framework for developing applications powered by language models."
    ]
    pipeline.ingest_documents(texts)
    assert pipeline.qa_chain is not None
    assert pipeline.vector_store is not None

def test_query(pipeline):
    texts = [
        "Python is a high-level programming language.",
        "Python is known for its simplicity and readability."
    ]
    pipeline.ingest_documents(texts)
    
    response = pipeline.query("What is Python?")
    assert isinstance(response, dict)
    assert "answer" in response
    assert "sources" in response
    assert len(response["sources"]) > 0