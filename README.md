# 🤖 CTAL-TAE AI Tutor

Agente de IA para auxiliar nos estudos da certificação **ISTQB CTAL-TAE (Test Automation Engineer)**.  
O sistema gera simulados automáticos, avalia respostas, explica conceitos e acompanha seu progresso.

---

## 🎯 Objetivo do Projeto

Este projeto foi criado para automatizar o estudo e prática da certificação **ISTQB CTAL-TAE**, permitindo:

- 🧠 Geração automática de simulados com base no syllabus oficial  
- ✅ Correção automática e explicações detalhadas  
- 📊 Acompanhamento de desempenho e progresso  
- 📚 Revisão personalizada por tópico  
- 🔗 Integração com modelos de linguagem (LLM) **open source e locais**

---

## ⚙️ Arquitetura do Sistema

```plaintext
Frontend (React + TypeScript + Vite)
│   ├── Simulados, flashcards e estatísticas
│
Backend (Python + FastAPI)
│   ├── API REST para geração, correção e progresso
│
LLM Provider (Ollama + Llama3)
│   ├── Geração de perguntas, feedback e explicações
│
Banco de Dados (PostgreSQL)
│   ├── Armazena usuários, simulados e desempenho
│
Vector DB (Weaviate)
│   ├── Busca semântica no syllabus
│
Fila (Redis + Celery)
│   ├── Processa geração assíncrona de simulados
│
CI/CD (GitHub Actions)
│   └── Build + Test + Deploy automático via Docker




| Componente         | Tecnologia                  | Descrição                 |
| ------------------ | --------------------------- | ------------------------- |
| **Backend**        | Python 3.11 + FastAPI       | API e orquestração da IA  |
| **Frontend**       | React + Vite + Tailwind     | Interface web moderna     |
| **LLM Provider**   | Ollama (Llama3)             | Modelo local open source  |
| **Banco de Dados** | PostgreSQL                  | Armazenamento persistente |
| **Vector DB**      | Weaviate                    | Busca semântica           |
| **Cache / Fila**   | Redis + Celery              | Processos assíncronos     |
| **Infraestrutura** | Docker + GitHub Actions     | Deploy contínuo           |
| **Monitoramento**  | Grafana + Sentry (opcional) | Logs e métricas           |


🚀 Como Começar (Setup Local)
1️⃣ Clonar o repositório

git clone https://github.com/eduardomoises/ctal-tae-ai-tutor.git
cd ctal-tae-ai-tutor


2️⃣ Criar arquivo .env na raiz

DATABASE_URL=postgresql://user:password@db:5432/ai_tutor
REDIS_URL=redis://redis:6379
PROVIDER=ollama
LLM_MODEL=llama3


**3️⃣ Instalar o LLM local (sem custo)

Baixe o Ollama → https://ollama.com/download**


**ollama pull llama3
ollama list
*4️⃣ Rodar Backend (modo local)

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Acesse:
👉 http://localhost:8000/docs

5️⃣ Rodar Frontend (modo local)
cd ../frontend
npm install
npm run dev


Acesse:
👉 http://localhost:5173

🐳 Executando com Docker
1️⃣ Subir o ambiente completo
docker-compose up --build

2️⃣ Containers disponíveis
Serviço	Função
backend	API FastAPI
frontend	App React
db	PostgreSQL
redis	Fila de tarefas
weaviate	Banco vetorial
ollama	Modelo Llama3 local
🧠 LLM Provider (Ollama)

O Ollama permite usar modelos locais de forma 100% gratuita.
Modelos recomendados:

ollama pull llama3
ollama pull mistral
ollama pull phi3


No .env, basta alternar:

LLM_MODEL=mistral

🔄 CI/CD – GitHub Actions

Arquivo: .github/workflows/ci-cd.yml

name: CI/CD
on: [push]
jobs:
  build-test-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: pip install -r backend/requirements.txt
      - name: Run tests
        run: pytest backend/tests
      - name: Build Docker
        run: docker-compose build
      - name: Deploy
        run: echo "🚀 (Deploy step - configure Render ou Vercel)"

📊 Observabilidade (opcional)
Ferramenta	Função
Sentry	Rastrear exceções do backend
Prometheus + Grafana	Métricas e monitoramento
Loki	Logs estruturados
🧠 Como Estudar com o Agente

Suba o projeto (docker-compose up)

Acesse http://localhost:5173

Escolha um capítulo do syllabus

Clique em Gerar Simulado

Responda → IA corrige e explica

Acompanhe seu progresso no dashboard

🪄 Próximas Etapas

💬 Chat com o syllabus (PDF + embeddings)

🧩 Revisão automática de tópicos fracos

🏆 Ranking e gamificação

🤖 Integração com Telegram Bot

🧰 Contribuição
git checkout -b feature/nova-funcionalidade
git commit -m "add: nova feature"
git push origin feature/nova-funcionalidade


Abra um Pull Request para revisão e integração.

👨‍💻 Autor

Eduardo Moises
QA Engineer | Test Automation | Cloud & DevOps
📧 contato: [seu-email]

🧾 Licença

Este projeto é distribuído sob a licença MIT – uso livre e open source.
📄 Consulte o arquivo LICENSE para mais detalhes.

🏷️ Badges





