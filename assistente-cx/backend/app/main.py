import os
import requests

# PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/assistente_cx")

# Ollama
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "ollama")
OLLAMA_PORT = int(os.getenv("OLLAMA_PORT", 11434))

OLLAMA_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"

def test_ollama():
    try:
        res = requests.get(f"{OLLAMA_URL}/health")
        if res.status_code == 200:
            print("Ollama OK!")
        else:
            print("Ollama retornou erro:", res.status_code)
    except Exception as e:
        print("Erro de conexão com Ollama:", e)
