from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from database import engine, SessionLocal
import models
import os
from routes.search import router as search_router
from routes.trending import router as trending_router
from routes.agents import router as agents_router

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
model = genai.GenerativeModel("gemini-2.5-flash")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
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

    # STEP 3 → fake AI answer
    response = model.generate_content(data.question)

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