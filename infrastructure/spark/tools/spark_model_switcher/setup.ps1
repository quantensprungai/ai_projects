$ErrorActionPreference = "Stop"

Write-Host "== Spark Model Switcher setup ==" -ForegroundColor Cyan

# Prefer Windows Python launcher (py) if available, otherwise python.
$pythonCmd = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
  $pythonCmd = "py -3"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
  $pythonCmd = "python"
}

function Resolve-PythonExe {
  # 1) Prefer py launcher if present
  if (Get-Command py -ErrorAction SilentlyContinue) { return "py -3" }

  # 2) python in PATH (but NOT WindowsApps alias)
  if (Get-Command python -ErrorAction SilentlyContinue) {
    try {
      $p = (Get-Command python -ErrorAction Stop).Source
      if ($p -notmatch "WindowsApps") { return "python" }
    } catch {}
  }

  # 3) Common install locations (winget/python.org)
  $candidates = @(
    "$env:LOCALAPPDATA\\Programs\\Python\\Python312\\python.exe",
    "$env:LOCALAPPDATA\\Programs\\Python\\Python311\\python.exe",
    "$env:LOCALAPPDATA\\Programs\\Python\\Python310\\python.exe",
    "$env:ProgramFiles\\Python312\\python.exe",
    "$env:ProgramFiles\\Python311\\python.exe",
    "$env:ProgramFiles\\Python310\\python.exe"
  )

  foreach ($c in $candidates) {
    if (Test-Path $c) { return $c }
  }

  return $null
}

$pythonCmd = Resolve-PythonExe

if (-not $pythonCmd) {
  Write-Host "Python wurde nicht gefunden (oder ist nur als WindowsApps-Alias vorhanden)." -ForegroundColor Red
  Write-Host "" 
  Write-Host "Dein winget sagt zwar 'installed', aber python ist nicht im PATH." -ForegroundColor Yellow
  Write-Host "Bitte fuehre aus und poste die Ausgabe:" -ForegroundColor Yellow
  Write-Host "  winget list --id Python.Python.3.12" -ForegroundColor Yellow
  Write-Host "  dir $env:LOCALAPPDATA\\Programs\\Python" -ForegroundColor Yellow
  Write-Host "" 
  Write-Host "Oder installiere erneut mit python.org Installer und 'Add to PATH' aktivieren." -ForegroundColor Yellow
  exit 1
}

Write-Host ("Using: " + $pythonCmd) -ForegroundColor Cyan

if (-not (Test-Path ".\\.venv")) {
  Write-Host "Creating venv..." -ForegroundColor Cyan
  if ($pythonCmd -eq "py -3") { py -3 -m venv .venv } else { & $pythonCmd -m venv .venv }
}

Write-Host "Installing requirements..." -ForegroundColor Cyan
.\.venv\Scripts\python -m pip install -r requirements.txt

if (-not (Test-Path ".\\config.json")) {
  Write-Host "Creating config.json from example..." -ForegroundColor Cyan
  Copy-Item .\\config.example.json .\\config.json
  Write-Host "Edit config.json and set spark.host (if needed)." -ForegroundColor Yellow
} else {
  Write-Host "config.json already exists (leaving as-is)." -ForegroundColor Green
}

Write-Host "Done. Start with:" -ForegroundColor Green
Write-Host "  .\\.venv\\Scripts\\python -m streamlit run app.py" -ForegroundColor Green

