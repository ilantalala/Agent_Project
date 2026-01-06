from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    messages: List[Message]


    model: Optional[str] = "gpt-4o-mini"
    system_prompt: Optional[str] = None
