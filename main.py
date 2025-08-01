import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

ALLOWED_USER_ID = "604346805"

class Message(BaseModel):
    user_id: str
    content: str

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/chat")
async def chat(msg: Message):
    if msg.user_id != ALLOWED_USER_ID:
        return {"error": "Access denied"}

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": msg.content}]
    )

    return {"reply": response["choices"][0]["message"]["content"]}
