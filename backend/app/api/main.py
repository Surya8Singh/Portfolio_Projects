# backend/app/api/main.py
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .models import QueryRequest, QueryResponse, Source
from ..core.rag_pipeline import RAGPipeline
from ..core.session_manager import SessionManager
import markdown
from typing import List 

# Initialize FastAPI app
app = FastAPI(title="Student Assistant API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG pipeline and session manager
rag_pipeline = RAGPipeline()
session_manager = SessionManager()

@app.post("/session")
async def create_session():
    session_id = session_manager.create_session()
    return {"session_id": session_id}

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    try:
        # Get or create session
        session_id = request.session_id or session_manager.create_session()
        
        # Get chat history
        chat_history = session_manager.get_history(session_id)
        
        # Get response
        response = rag_pipeline.query(
            question=request.question,
            chat_history=chat_history
        )
        
        # Add to history
        session_manager.add_to_history(session_id, "user", request.question)
        session_manager.add_to_history(session_id, "assistant", response["answer"])
        
        return QueryResponse(
            answer=response["answer"],
            formatted_answer=response["formatted_answer"],
            sources=[Source(content=s["content"], metadata=s["metadata"]) 
                    for s in response["sources"]]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history/{session_id}")
async def get_chat_history(session_id: str):
    try:
        history = session_manager.get_history(session_id)
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Session not found")

# Keep the file upload endpoint
@app.post("/upload")
async def upload_documents(files: List[UploadFile] = File(...)):
    try:
        documents = []
        for file in files:
            content = await file.read()
            text = content.decode("utf-8")
            documents.append(text)
        
        rag_pipeline.ingest_documents(documents)
        return {"message": f"Successfully processed {len(documents)} documents"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}