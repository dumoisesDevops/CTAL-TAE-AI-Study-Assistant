# Caminho do Ollama
$ollamaPath = "C:\Users\User\AppData\Local\Programs\Ollama\ollama.exe"

# Porta que o Ollama usa
$ollamaPort = 11434

# Função para verificar se a porta está em uso
function Test-Port($port) {
    $tcp = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
    return $tcp -ne $null
}

# Inicia o Ollama se não estiver rodando
if (-not (Test-Port $ollamaPort)) {
    Write-Host "Iniciando Ollama..."
    Start-Process -NoNewWindow -FilePath $ollamaPath -ArgumentList "serve"
} else {
    Write-Host "Ollama já está rodando na porta $ollamaPort"
}

# Aguarda Ollama ficar pronto
Write-Host "Aguardando Ollama..."
while (-not (Test-Port $ollamaPort)) {
    Start-Sleep -Seconds 2
}
Write-Host "Ollama está pronto!"

# Sobe o Docker Compose
Write-Host "Iniciando Docker Compose..."
docker compose up --build
