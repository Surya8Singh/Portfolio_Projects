# backend/app/core/vector_store.py
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings  # Updated import
import os
from dotenv import load_dotenv

load_dotenv()

class VectorStore:
    def __init__(self):
        """Initialize the vector store with OpenAI embeddings"""
        self.embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
        self.vector_store = None
        self.vector_store_path = os.getenv("VECTOR_DB_PATH", "./vector_storage")

    def initialize_store(self, texts):
        """Initialize vector store with documents"""
        if not os.path.exists(self.vector_store_path):
            os.makedirs(os.path.dirname(self.vector_store_path), exist_ok=True)
            self.vector_store = FAISS.from_texts(texts, self.embeddings)
            self.vector_store.save_local(self.vector_store_path)
        else:
            self.vector_store = FAISS.load_local(
                self.vector_store_path,
                self.embeddings,
                allow_dangerous_deserialization=True  # Only for testing purposes
            )

    def similarity_search(self, query: str, k: int = 3):
        """Search for similar documents"""
        if not self.vector_store:
            raise ValueError("Vector store not initialized. Call initialize_store first.")
        return self.vector_store.similarity_search(query, k=k)

    def add_texts(self, texts: list[str]):
        """Add new texts to the vector store"""
        if not self.vector_store:
            self.initialize_store(texts)
        else:
            self.vector_store.add_texts(texts)
            self.vector_store.save_local(self.vector_store_path)