# backend/app/core/session_manager.py
from typing import Dict, List, Tuple
from ..api.models import ChatHistory
import uuid

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, ChatHistory] = {}

    def create_session(self) -> str:
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = ChatHistory()
        return session_id

    def get_session(self, session_id: str) -> ChatHistory:
        if session_id not in self.sessions:
            session_id = self.create_session()
        return self.sessions[session_id]

    def add_to_history(self, session_id: str, role: str, content: str):
        session = self.get_session(session_id)
        session.add_message(role, content)

    def get_history(self, session_id: str) -> List[Tuple[str, str]]:
        session = self.get_session(session_id)
        return session.get_history()