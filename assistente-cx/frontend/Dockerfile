# frontend/Dockerfile
FROM node:20-alpine

WORKDIR /app

# Copia package.json e package-lock.json se existir
COPY package*.json ./

# Instala build tools e dependências
RUN apk add --no-cache make g++ python3 \
    && npm install \
    && npm rebuild

# Copia todo o código
COPY . .

# Expõe a porta do Vite
EXPOSE 5173

# Comando para rodar o frontend
CMD ["npm", "run", "dev"]
