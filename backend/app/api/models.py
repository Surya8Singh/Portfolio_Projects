# backend/app/api/models.py
from pydantic import BaseModel
from typing import List, Optional, Dict, Tuple

class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class ChatHistory:
    def __init__(self):
        self.messages: List[Message] = []

    def add_message(self, role: str, content: str):
        self.messages.append(Message(role=role, content=content))

    def get_history(self) -> List[Tuple[str, str]]:
        return [(msg.role, msg.content) for msg in self.messages]

class QueryRequest(BaseModel):
    question: str
    session_id: Optional[str] = None
    chat_history: Optional[List[Tuple[str, str]]] = []

class Source(BaseModel):
    content: str
    metadata: Optional[Dict] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
    formatted_answer: str