from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import gerar_questoes

router = APIRouter()

# Model para receber JSON
class SimuladoRequest(BaseModel):
    topic: str

@router.post("/create")
async def create_simulado(request: SimuladoRequest):
    topic = request.topic
    questoes = await gerar_questoes(topic)
    return {"topic": topic, "questoes": questoes}
