import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"
    assert "llm_provider" in res.json()

def test_ai_categorize():
    res = client.post("/api/v1/ai/categorize", json={"text": "How do I renew my annual billing invoice credit card?"})
    assert res.status_code == 200
    assert res.json()["category"] == "BILLING"

def test_ai_suggest_reply():
    res = client.post("/api/v1/ai/suggest-reply", json={
        "subject": "VPN Authentication Failure",
        "content": "SAML 2.0 login timeout error 500"
    })
    assert res.status_code == 200
    assert "suggested_reply" in res.json()

def test_ticket_ingestion_and_rag():
    # Ingest Ticket
    ingest_res = client.post("/api/v1/tickets", json={
        "customer_email": "client@enterprise.com",
        "subject": "Payment Gate Failure",
        "content": "Credit card billing processing failed on subscription renewal."
    })
    assert ingest_res.status_code == 200
    assert ingest_res.json()["category"] == "BILLING"

    # Add Knowledge Base Doc
    kb_res = client.post("/api/v1/knowledge-base", json={
        "title": "Resolving Billing & Payment Failures",
        "content": "Verify credit card expiration date and billing address in account settings.",
        "category": "BILLING"
    })
    assert kb_res.status_code == 200

    # Vector Search
    search_res = client.get("/api/v1/knowledge-base/search?query=billing+payment")
    assert search_res.status_code == 200
    assert len(search_res.json()) > 0
