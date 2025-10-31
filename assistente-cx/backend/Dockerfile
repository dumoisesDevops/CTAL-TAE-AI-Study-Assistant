# Use Python 3.12 slim como base
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de requirements primeiro (para aproveitar cache do Docker)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando padrão para iniciar o backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
