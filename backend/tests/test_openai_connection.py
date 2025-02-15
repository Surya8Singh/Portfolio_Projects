import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

def test_openai_connection():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    assert api_key is not None, "OPENAI_API_KEY not found in environment variables"
    
    # Initialize client without any extra arguments
    client = OpenAI()  # OpenAI will automatically use the OPENAI_API_KEY from environment
    
    try:
        # Test with a simple embedding
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input="Hello, world!"
        )
        
        assert response.data[0].embedding is not None
        assert len(response.data[0].embedding) > 0
    except Exception as e:
        print(f"Error during API call: {str(e)}")
        raise