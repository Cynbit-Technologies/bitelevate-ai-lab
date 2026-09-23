import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, DateTime, Float, JSON, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(String, primary_key=True, default=generate_uuid)
    customer_email = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(100), default="UNCATEGORIZED")
    sentiment = Column(String(50), default="NEUTRAL")
    ai_suggested_reply = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class KnowledgeDoc(Base):
    __tablename__ = "knowledge_docs"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
