# ReelButler

ReelButler is an AI-powered Creator Intelligence Platform that automates viral content research, trend analysis, and short-form content generation for influencers using real-time YouTube trend data, Retrieval-Augmented Generation (RAG), and multi-agent AI workflows.

---

## Features

- Real-time YouTube Shorts trend ingestion
- Historical engagement tracking and analytics
- Semantic trend search using FAISS + BM25
- Multi-agent AI workflows
- AI-powered script generation
- Audience psychology analysis
- Hashtag optimization
- Trend analytics dashboard
- AI Creator Studio
- Hybrid Retrieval Architecture (Semantic + Keyword Search)

---

## AI Agents

### Trend Analyzer Agent
Analyzes viral patterns, creator strategies, and trend opportunities.

### Script Generator Agent
Generates hooks, scripts, CTAs, editing suggestions, and creator recommendations.

### Psychology Agent
Identifies emotional triggers, curiosity gaps, FOMO mechanisms, and retention strategies.

### Hashtag Agent
Generates SEO-optimized and niche-specific hashtag strategies.

### Orchestrator Agent
Coordinates multiple AI agents into a unified creator workflow.

---

## System Architecture

```text
YouTube API
      ↓
Data Ingestion Pipeline
      ↓
PostgreSQL + Historical Metrics
      ↓
Embeddings Generation
      ↓
FAISS + BM25 Hybrid Retrieval
      ↓
Multi-Agent AI System
      ↓
React Dashboard + Creator Studio

## Tech Stack

### Backend
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- APScheduler

### AI / ML
- Gemini API
- Sentence Transformers
- FAISS
- BM25
- RAG Architecture
- Machine Learning

### Frontend
- React
- Vite
- Recharts

## Setup Instructions

### Clone Repository

```bash
git clone <repo-url>

cd ReelButler
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Frontend Setup

```bash
cd frontend

npm install
```

---

## Environment Variables

Create a `.env` file inside `backend/`

```env
GEMINI_API_KEY=your_key

YOUTUBE_API_KEY=your_key

DATABASE_URL=your_database_url
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

---

## Run Frontend

```bash
npm run dev
```

---

## Future Improvements

- ML-based trend forecasting
- Personalized creator recommendations
- Redis caching
- JWT authentication
- Advanced creator analytics
- Deployment using Vercel + Render

---

## Author

Karan Jangra