$targetDir = "C:\Jarvis\DEV\jarvis-painel"

Write-Host "Iniciando instalacao do Painel Jarvis..." -ForegroundColor Cyan

# 1. Clonar o repositorio
if (-not (Test-Path $targetDir)) {
    Write-Host "Clonando repositorio..." -ForegroundColor Yellow
    git clone https://github.com/melgarafael/james_painel_de_voz.git $targetDir
} else {
    Write-Host "A pasta $targetDir ja existe." -ForegroundColor Yellow
}

cd $targetDir

# 2. Renomear 'James' para 'Jarvis' nos arquivos
Write-Host "Renomeando 'James' para 'Jarvis' na interface..." -ForegroundColor Yellow
$filesToEdit = Get-ChildItem -Path ".\src", ".\index.html" -Recurse -File -Include *.tsx, *.ts, *.html, *.css, *.json

foreach ($file in $filesToEdit) {
    $originalContent = Get-Content $file.FullName -Raw
    if ($originalContent -match "(?i)james") {
        # Faz replace mantendo maiusculas/minusculas quando possivel, ou forcando Jarvis
        $newContent = $originalContent -creplace "James", "Jarvis" -creplace "james", "jarvis" -creplace "JAMES", "JARVIS"
        Set-Content -Path $file.FullName -Value $newContent
        Write-Host "  Atualizado: $($file.Name)" -ForegroundColor DarkGray
    }
}

# 3. Instalar dependencias
Write-Host "Instalando dependencias (isso pode demorar um pouco)..." -ForegroundColor Yellow
npm install

# 4. Iniciar o servidor
Write-Host "Tudo pronto! Iniciando o Jarvis no localhost..." -ForegroundColor Green
npm run dev
