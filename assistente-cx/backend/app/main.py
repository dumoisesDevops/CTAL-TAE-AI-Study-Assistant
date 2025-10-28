from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Assistente CX API")

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API Assistente CX rodando 🎯"}

@app.post("/analyze")
def analyze_message(msg: Message):
    return {"reply": f"Analisando sua mensagem: {msg.text}"}
