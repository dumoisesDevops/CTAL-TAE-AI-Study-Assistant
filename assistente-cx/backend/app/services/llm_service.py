import httpx, os

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = os.getenv("LLM_MODEL", "llama3")

async def gerar_questoes(topic: str):
    prompt = f"Crie 3 questões objetivas sobre o tema '{topic}' do ISTQB CTAL-TAE."
    async with httpx.AsyncClient() as client:
        response = await client.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False})
        data = response.json()
        return data.get("response", "Nenhuma questão gerada.")
