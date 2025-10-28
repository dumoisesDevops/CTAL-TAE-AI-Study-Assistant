from fastapi import APIRouter
from app.services.llm_service import gerar_questoes

router = APIRouter()

@router.post("/create")
async def create_simulado(topic: str):
    questoes = await gerar_questoes(topic)
    return {"topic": topic, "questoes": questoes}
