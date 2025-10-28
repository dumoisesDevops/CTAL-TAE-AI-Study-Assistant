Write-Host "============================="
Write-Host "HEALTH CHECK - ASSISTENTE CX"
Write-Host "============================="

# 1. Containers
Write-Host "`nContainers em execucao..."
$containers = docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
if ($containers) {
    Write-Host $containers
} else {
    Write-Host "Nenhum container esta em execucao!"
    exit 1
}

# 2. Backend
Write-Host "`nTestando backend (http://localhost:8000/docs)..."
try {
    $backend = Invoke-WebRequest "http://localhost:8000/docs" -UseBasicParsing -TimeoutSec 5
    if ($backend.StatusCode -eq 200) {
        Write-Host "Backend ativo!"
    } else {
        Write-Host "Backend respondeu com status: $($backend.StatusCode)"
    }
} catch {
    Write-Host "Backend nao respondeu!"
}

# 3. Frontend
Write-Host "`nTestando frontend (http://localhost:5173)..."
try {
    $frontend = Invoke-WebRequest "http://localhost:5173" -UseBasicParsing -TimeoutSec 5
    if ($frontend.StatusCode -eq 200) {
        Write-Host "Frontend ativo!"
    } else {
        Write-Host "Frontend respondeu com status: $($frontend.StatusCode)"
    }
} catch {
    Write-Host "Frontend nao respondeu!"
}

# 4. PostgreSQL
Write-Host "`nTestando PostgreSQL..."
$portCheck = Test-NetConnection -ComputerName "localhost" -Port 5432
if ($portCheck.TcpTestSucceeded) {
    Write-Host "PostgreSQL acessivel na porta 5432!"
} else {
    Write-Host "PostgreSQL nao esta acessivel!"
}

Write-Host "`nHealth-check concluido!"
