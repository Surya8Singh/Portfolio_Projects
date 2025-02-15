import os
import openai
from dotenv import load_dotenv

def test_minimal_openai():
    # Load environment variables
    load_dotenv()
    
    # Get API key and set it
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
    
    # Test with a simple API call
    try:
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input="Hello, world!"
        )
        assert response['data'][0]['embedding'] is not None
    except Exception as e:
        print(f"Error details: {str(e)}")
        raise