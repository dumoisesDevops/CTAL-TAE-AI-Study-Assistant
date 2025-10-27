🎯 Objetivo do Projeto

Este projeto implementa um Agente de IA para auxiliar nos estudos da certificação ISTQB CTAL-TAE (Test Automation Engineer).
O sistema permite:

Geração de simulados automáticos com base no syllabus oficial;

Avaliação de respostas e explicações detalhadas;

Acompanhamento de desempenho e progresso;

Revisão personalizada por tópico;

Integração com LLMs (OpenAI / Amazon Bedrock / modelo local).

⚙️ Arquitetura do Sistema
Frontend (React + TypeScript + Vite)
│
├── Simulados, flashcards e estatísticas
│
Backend (Python + FastAPI)
│
├── API REST para geração, correção e progresso
│
LLM Provider (OpenAI / Bedrock / Local)
│
├── Geração de questões, feedback e explicações
│
Banco de Dados (PostgreSQL)
│
├── Armazena usuários, simulados e desempenho
│
Vector DB (Weaviate / Milvus)
│
├── Armazena embeddings do syllabus
│
Fila (Redis + Celery)
│
├── Processa geração assíncrona de simulados
│
CI/CD (GitHub Actions)
│
└── Build + Test + Deploy automático via Docker

🧩 Stack Técnica
Componente	Tecnologia	Descrição
Backend	Python 3.11 + FastAPI	API e orquestração da IA
Frontend	React + Vite + Tailwind CSS	Interface web moderna
LLM Provider	OpenAI / Amazon Bedrock	Geração de perguntas e explicações
Banco de Dados	PostgreSQL	Armazenamento persistente
Vector DB	Weaviate / Milvus	Busca semântica no syllabus
Cache/Fila	Redis + Celery	Processos assíncronos
Infra	Docker + GitHub Actions	Automação e deploy contínuo
Observabilidade	Sentry + Grafana (opcional)	Monitoramento e logs
🚀 Como Começar (Setup Local)
1️⃣ Clonar o repositório
git clone https://github.com/<seu-usuario>/ctal-tae-ai-tutor.git
cd ctal-tae-ai-tutor

2️⃣ Estrutura inicial
ctal-tae-ai-tutor/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   └── models/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── vite.config.ts
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── .github/workflows/ci-cd.yml

🧱 Backend – Setup e Execução
1️⃣ Instalar dependências (modo local)
cd backend
pip install -r requirements.txt

2️⃣ Rodar localmente (modo dev)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

3️⃣ Endpoints principais
Método	Endpoint	Função
POST	/api/simulado/create	Gera um simulado baseado no syllabus
POST	/api/simulado/submit	Envia respostas e calcula pontuação
GET	/api/syllabus/search	Busca trechos do syllabus
GET	/api/progress/{user_id}	Retorna estatísticas de estudo
🖥️ Frontend – Setup e Execução
1️⃣ Instalar dependências
cd frontend
npm install

2️⃣ Rodar localmente
npm run dev

3️⃣ Estrutura inicial do front

/simulado → faz requisição ao backend para gerar questões.

/dashboard → exibe progresso e recomendações.

/login → autenticação via JWT.

🐳 Executando com Docker
1️⃣ Criar .env na raiz:
OPENAI_API_KEY=sk-xxxxxx
DATABASE_URL=postgresql://user:password@db:5432/ai_tutor
REDIS_URL=redis://redis:6379
PROVIDER=openai

2️⃣ Subir o ambiente completo:
docker-compose up --build


Containers:

backend → API FastAPI

frontend → React App

db → PostgreSQL

redis → Fila de tarefas

weaviate → Vector DB

🧠 LLM Providers (Configuração)
🔹 OpenAI (recomendado para início)

Crie uma conta em https://platform.openai.com

Pegue sua API Key

Configure no .env:

PROVIDER=openai
OPENAI_API_KEY=sk-xxxxx

🔹 Amazon Bedrock

Ative o Bedrock na sua conta AWS.

Crie um usuário IAM com permissão bedrock:* e gere credenciais.

Configure no .env:

PROVIDER=bedrock
AWS_ACCESS_KEY_ID=xxxx
AWS_SECRET_ACCESS_KEY=xxxx
AWS_REGION=us-east-1

🔄 CI/CD – GitHub Actions

.github/workflows/ci-cd.yml

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
        run: echo "🚀 (Deploy step - configure ECS, Railway, Render ou Vercel)"

📊 Observabilidade

Sentry → rastrear exceções do backend.

Prometheus + Grafana → monitorar uso de CPU, memória e latência da API.

Logs estruturados → enviados para CloudWatch (AWS) ou Loki.

🧠 Como estudar com o agente

Suba o projeto com docker-compose up.

Abra http://localhost:5173.

Escolha um capítulo do syllabus.

Clique em Gerar Simulado → IA cria questões com base no tópico.

Responda → IA corrige e explica.

Veja seu progresso no dashboard.

🪄 Próximas Etapas

 Adicionar modo “Chat com o Syllabus” (tipo ChatGPT sobre o PDF).

 Adicionar ranking e comparativo de performance.

 Integrar API do Telegram para responder via chat.

 Implementar modo “Revisão Automática” (IA sugere o que revisar).

🧰 Contribuição
git checkout -b feature/nova-funcionalidade
git commit -m "add: nova feature"
git push origin feature/nova-funcionalidade


Abra um Pull Request para revisão e integração.

👨‍💻 Autor

Eduardo Moises
QA Engineer | Test Automation | Cloud & DevOps
📧 contato: [seu-email]
🌐 GitHub: [github.com/seu-usuario]
