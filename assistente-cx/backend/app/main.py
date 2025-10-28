from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.routes.simulado import router as simulado_router  # importar a rota de simulados

app = FastAPI(title="Assistente CX API")

# CORS para frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas de simulados
app.include_router(simulado_router, prefix="/simulado")

# Rotas de teste existentes
class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API Assistente CX rodando 🎯"}

@app.post("/analyze")
def analyze_message(msg: Message):
    return {"reply": f"Analisando sua mensagem: {msg.text}"}
