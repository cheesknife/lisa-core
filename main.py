from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

class Message(BaseModel):
    user_id: str
    content: str

@app.post("/chat")
async def chat(msg: Message):
    import os
openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": msg.content}]
    )
    return {"reply": response.choices[0].message["content"]}
