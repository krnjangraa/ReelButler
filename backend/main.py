from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from database import engine, SessionLocal
import models
import os
from routes.search import router as search_router
from routes.trending import router as trending_router
from routes.agents import router as agents_router
from fastapi.middleware.cors import (
    CORSMiddleware
)
# from scheduler import start_scheduler

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

models.Base.metadata.create_all(
    bind=engine
)

app = FastAPI()
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)
# start_scheduler()
app.include_router(trending_router)
app.include_router(search_router)
app.include_router(agents_router)

class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(data: QuestionRequest):

    db = SessionLocal()

    # STEP 1 → check if already exists
    existing = db.query(models.Inquiry).filter(
        models.Inquiry.question == data.question
    ).first()

    # STEP 2 → return cached answer
    if existing:
        return {
            "answer": existing.answer,
            "cached": True
        }

    # STEP 3 → generate answer
    response = client.models.generate_content(

    model="gemini-2.5-flash",

    contents=data.question
    )

    answer = response.text

    # STEP 4 → store in DB
    new_entry = models.Inquiry(
        question=data.question,
        answer=answer
    )

    db.add(new_entry)

    db.commit()

    return {
        "answer": answer,
        "cached": False
    }