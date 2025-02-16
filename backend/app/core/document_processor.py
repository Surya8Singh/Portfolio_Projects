from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
import re

class DocumentProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """Initialize the document processor
        
        Args:
            chunk_size: The size of each text chunk
            chunk_overlap: The amount of overlap between chunks
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

    def clean_text(self, text: str) -> str:
        """Clean the text by removing extra whitespace and special characters
        
        Args:
            text: The text to clean
        
        Returns:
            str: The cleaned text
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep punctuation
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()

    def process_document(self, text: str) -> List[str]:
        """Process a document into chunks
        
        Args:
            text: The document text to process
        
        Returns:
            List[str]: List of text chunks
        """
        # Clean the text
        cleaned_text = self.clean_text(text)
        # Split into chunks
        return self.text_splitter.split_text(cleaned_text)