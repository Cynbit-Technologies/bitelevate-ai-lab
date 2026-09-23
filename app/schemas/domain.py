from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional, List
from datetime import datetime

class TicketIngest(BaseModel):
    customer_email: EmailStr
    subject: str
    content: str

class TicketResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    customer_email: str
    subject: str
    content: str
    category: str
    sentiment: str
    ai_suggested_reply: Optional[str]
    created_at: datetime

class CategorizeRequest(BaseModel):
    text: str

class CategorizeResponse(BaseModel):
    category: str
    confidence: float

class SuggestReplyRequest(BaseModel):
    subject: str
    content: str

class SuggestReplyResponse(BaseModel):
    suggested_reply: str
    provider: str

class KnowledgeDocCreate(BaseModel):
    title: str
    content: str
    category: str

class KnowledgeDocResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    title: str
    content: str
    category: str
    created_at: datetime

class KBSearchResponse(BaseModel):
    doc_id: str
    title: str
    snippet: str
    similarity_score: float
