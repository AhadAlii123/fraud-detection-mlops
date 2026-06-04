Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "🚀 Starting Automated CI/CD Deployment Process..." -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# 1. Purane chalte hue container ko check karke remove karna
Write-Host "🧹 Checking for existing container..." -ForegroundColor Yellow
$oldContainer = docker ps -a -q --filter "name=fraud-api-container"
if ($oldContainer) {
    Write-Host "Stopping and removing old container..." -ForegroundColor Gray
    docker stop fraud-api-container
    docker rm fraud-api-container
}

# 2. Fresh Docker Image Build karna
Write-Host "🏗️ Building fresh Docker Image..." -ForegroundColor Yellow
docker build -t fraud-detection-image .

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Docker build failed!" -ForegroundColor Red
    Exit
}

# 3. Naye Container ko run karna
Write-Host "🚢 Deploying new container into production..." -ForegroundColor Yellow
docker run -d -p 8000:8000 --name fraud-api-container fraud-detection-image

# 4. Status Check
Write-Host "=============================================" -ForegroundColor Green
Write-Host "✅ Deployment Successful! API is Live on Port 8000." -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green