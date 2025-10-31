# app/config.py

# URL do serviço Ollama (ajuste se estiver rodando em outro host/porta)
OLLAMA_URL = "http://host.docker.internal:11434/api/generate"  # 'host.docker.internal' funciona para Docker no Windows/Mac

# Modelo que você quer usar
MODEL = "llama3"  # substitua pelo nome do modelo que você tiver no Ollama

