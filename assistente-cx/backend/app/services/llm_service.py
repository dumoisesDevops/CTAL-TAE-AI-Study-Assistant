import httpx
import json
from app.config import OLLAMA_URL, MODEL  # ajuste conforme seu projeto

async def gerar_questoes(topic: str):
    prompt = f"Crie questões sobre o tema: {topic}"

    async with httpx.AsyncClient(timeout=60) as client:  # Timeout maior
        try:
            response = await client.post(
                OLLAMA_URL,
                json={"model": MODEL, "prompt": prompt, "stream": False}
            )

            # Tentar interpretar como JSON direto
            try:
                data = response.json()
                # Se a resposta tiver chave específica, retorne as questões
                if "questions" in data:
                    return data["questions"]
                return data
            except json.JSONDecodeError:
                # Se falhar, tenta tratar como texto bruto
                raw_text = await response.aread() if hasattr(response, "aread") else response.text
                raw_text = raw_text.decode() if isinstance(raw_text, bytes) else raw_text
                print("Resposta do Ollama não é JSON válido:")
                print(raw_text)

                # Tenta extrair JSON do texto (caso venha texto + JSON)
                try:
                    start = raw_text.find("{")
                    end = raw_text.rfind("}") + 1
                    json_data = json.loads(raw_text[start:end])
                    return json_data.get("questions", json_data)
                except Exception:
                    # Retorna fallback seguro
                    return [{"question": f"Não foi possível gerar questão para: {topic}"}]

        except httpx.RequestError as e:
            print(f"Erro de conexão com Ollama: {e}")
            return [{"question": f"Erro de conexão ao gerar questão para: {topic}"}]
