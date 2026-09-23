# SupportPulse AI Platform (`bitelevate-ai-lab`)

> Support Intelligence Platform featuring AI ticket categorization, automated response generation, and vector-search RAG knowledge base.

---

## 1. What the Project Is

**SupportPulse AI Platform** is a customer support intelligence API. It ingests support tickets, performs automated category classification, generates suggested AI responses, and executes vector similarity search across a RAG knowledge base.

---

## 2. Technology Stack

- **Framework**: FastAPI (Python 3.11+)
- **Database & ORM**: SQLAlchemy 2.0, PostgreSQL / SQLite
- **LLM Engine**: LiteLLM + Offline Mock Provider (no paid API key required for offline runs)
- **Vector Search**: Cosine similarity embedding search foundation

---

## 3. How to Run Locally

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start API Server**:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   - API Docs: `http://localhost:8000/docs`
   - Health Check: `http://localhost:8000/health`

---

## 4. Environment Variables

Copy `.env.example` to `.env`:

```env
LLM_PROVIDER="mock"  # Use "mock" for zero-cost local execution
OPENAI_API_KEY=""
DATABASE_URL="sqlite:///./support_ai.db"
```

---

## 5. Project Structure

```
bitelevate-ai-lab/
├── app/
│   ├── api/v1/          # Endpoints (tickets, AI categorize, suggest-reply, RAG search)
│   ├── core/            # App configuration
│   ├── models/          # Ticket and KnowledgeDoc models
│   ├── schemas/         # Pydantic validation schemas
│   ├── services/        # LLM provider & vector similarity search engine
│   └── main.py          # Entry point
├── tests/
│   └── test_ai_api.py   # Pytest suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── SECURITY.md
```

---

## 6. How to Run Tests

```bash
python -m pytest -v
```

---

## 7. How to Contribute

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for contribution guidelines.
# bitelevate-ai-lab
