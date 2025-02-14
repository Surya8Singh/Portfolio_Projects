# test file
def test_imports():
    try:
        import fastapi
        import uvicorn
        import langchain
        import openai
        import dotenv
        import pytest
        import httpx
        print("All packages imported successfully!")
    except ImportError as e:
        print(f"Error importing packages: {e}")

if __name__ == "__main__":
    test_imports()