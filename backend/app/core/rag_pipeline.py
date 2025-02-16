# backend/app/core/rag_pipeline.py
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from .document_processor import DocumentProcessor
from langchain_openai import OpenAIEmbeddings  # Add this import
import os
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
import markdown
from typing import Dict, Any, List


load_dotenv()

class RAGPipeline:
    def __init__(self, persist_directory: str = "./chroma_db"):
        """Initialize the RAG pipeline
        
        Args:
            persist_directory: Directory to store the vector database
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
            
        self.document_processor = DocumentProcessor()
        self.embeddings = OpenAIEmbeddings(api_key=api_key)
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            api_key=api_key
        )
        
        # Set up vector store directory
        self.vector_store_path = persist_directory
        Path(self.vector_store_path).mkdir(parents=True, exist_ok=True)
        
        self.vector_store = None
        self.qa_chain = None

    def ingest_documents(self, texts: List[str]) -> None:
        """Ingest documents into the vector store"""
        # Process documents into chunks
        processed_chunks = []
        for text in texts:
            chunks = self.document_processor.process_document(text)
            processed_chunks.extend(chunks)
        
        # Create or get vector store
        self.vector_store = Chroma.from_texts(
            texts=processed_chunks,
            embedding=self.embeddings,
            persist_directory=self.vector_store_path
        )
        
        # Initialize QA chain
        self._initialize_qa_chain()

    def _initialize_qa_chain(self) -> None:
        """Initialize the QA chain"""
        if not self.vector_store:
            raise ValueError("Vector store not initialized")
            
        retriever = self.vector_store.as_retriever(
            search_kwargs={"k": 3}
        )
        
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            return_source_documents=True
        )

    def query(self, 
             question: str, 
             chat_history: Optional[List[tuple]] = None) -> Dict[str, Any]:
        """Query the RAG pipeline"""
        if not self.qa_chain:
            raise ValueError("Pipeline not initialized. Ingest documents first.")
        
        if chat_history is None:
            chat_history = []
            
        try:
            response = self.qa_chain(
                {"question": question, "chat_history": chat_history}
            )
            
            return {
                "answer": response["answer"],
                "sources": [doc.page_content for doc in response["source_documents"]]
            }
        except Exception as e:
            raise ValueError(f"Error during query: {str(e)}")
        
    def format_response(self, answer: str) -> str:
        """Format the response in markdown"""
        # Add markdown formatting
        formatted = answer.replace('\n', '\n\n')  # Better paragraph spacing
        # Add highlighting for code blocks, if any
        formatted = formatted.replace('```python', '\n```python\n')
        return markdown.markdown(formatted)

    def query(self, 
             question: str, 
             chat_history: Optional[List[tuple]] = None) -> Dict[str, Any]:
        """Enhanced query with formatted response"""
        if not self.qa_chain:
            raise ValueError("Pipeline not initialized. Ingest documents first.")
        
        if chat_history is None:
            chat_history = []
            
        try:
            response = self.qa_chain({
                "question": question,
                "chat_history": chat_history
            })
            
            answer = response["answer"]
            sources = response["source_documents"]
            
            return {
                "answer": answer,
                "formatted_answer": self.format_response(answer),
                "sources": [
                    {
                        "content": doc.page_content,
                        "metadata": doc.metadata
                    } for doc in sources
                ]
            }
        except Exception as e:
            raise ValueError(f"Error during query: {str(e)}")