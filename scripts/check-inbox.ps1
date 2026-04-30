# Jarvis Inbox Monitor — Task Scheduler durable cron
# Roda a cada 2 min. Detecta PENDING no inbox.md → dispara claude -p → processa cadeia.

$vaultPath = "C:\JARVIS"
$inboxPath = "$vaultPath\00 - Jarvis\shared\inbox.md"
$logPath = "$vaultPath\scripts\inbox-monitor.log"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$ts | $msg" | Out-File -Append -FilePath $logPath
}

Set-Location $vaultPath

# Pull latest
$pullResult = git pull --quiet 2>&1
Log "git pull: $pullResult"

# Check for PENDING
$inbox = Get-Content $inboxPath -Raw -ErrorAction SilentlyContinue
if (-not $inbox) {
    Log "inbox.md vazio ou não encontrado"
    exit 0
}

if ($inbox -notmatch "STATUS: PENDING") {
    Log "sem tasks PENDING"
    exit 0
}

Log "PENDING detectado — disparando jarvis-ceo"

# Build prompt
$prompt = @"
Você é o jarvis-ceo. Leia o arquivo C:\JARVIS\00 - Jarvis\shared\inbox.md.
Encontre a task com STATUS: PENDING mais antiga.
Execute a cadeia de agentes necessária para completar a task.
Ao finalizar:
1. Escreva o resultado em C:\JARVIS\00 - Jarvis\shared\outbox.md
2. Mude o STATUS da task no inbox.md de PENDING para DONE
3. Faça git add, git commit e git push com mensagem: "task: [nome da task] processada pelo escritório"
Formato outbox.md:
STATUS: DONE
TASK: [nome]
RESULT: [resultado completo]
COMPLETED: [timestamp]
"@

# Run claude headless
claude --dangerously-skip-permissions -p $prompt

Log "claude -p finalizado"

# Push result
git add -A
$commitMsg = "task: inbox processado pelo escritorio local $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git commit -m $commitMsg 2>&1 | Out-Null
git push --quiet 2>&1 | Out-Null
Log "git push feito"
