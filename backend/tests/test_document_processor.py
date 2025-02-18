import pytest
from app.core.document_processor import DocumentProcessor

@pytest.fixture
def processor():
    return DocumentProcessor()

def test_clean_text(processor):
    text = """This is a    test
    with multiple spaces   and
    newlines."""
    cleaned = processor.clean_text(text)
    assert "  " not in cleaned
    assert cleaned.count("\n") == 0

def test_process_document(processor):
    text = "This is a " * 500  # Create a long document
    chunks = processor.process_document(text)
    assert len(chunks) > 1
    assert all(len(chunk) <= 1000 for chunk in chunks)