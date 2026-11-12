param(
    [Parameter(Mandatory = $false)]
    [ValidatePattern('^S\d{2}$')]
    [string]$Session = "S00"
)

$ErrorActionPreference = "Stop"
$RepoRoot   = Split-Path -Parent $PSScriptRoot
$BackendDir = Join-Path $RepoRoot "eshop-sut\backend"
$WebDir     = Join-Path $RepoRoot "eshop-sut\frontend-web"
$HelperFile = Join-Path $PSScriptRoot "session_helper.html"

Write-Host "=== KHOI TAO TRAM THU NGHIEM USABILITY SACH CHO PHIEN $Session ===" -ForegroundColor Cyan

# 1. Dung Backend cu tren cong 3000 (neu co)
$port3000 = Get-NetTCPConnection -LocalPort 3000 -State Listen -ErrorAction SilentlyContinue
if ($port3000) {
    $procIds = $port3000 | Select-Object -ExpandProperty OwningProcess -Unique
    foreach ($procId in $procIds) {
        Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
    }
    Start-Sleep -Milliseconds 700
}

# 2. Xoa database.sqlite de node server.js tu dong init & seed CSDL sach moi tinh
$dbFile = Join-Path $BackendDir "database.sqlite"
if (Test-Path $dbFile) {
    Remove-Item -Force $dbFile
}
Write-Host "[1/4] Da xoa database.sqlite cu de khoi tao Clean State." -ForegroundColor Green

# 3. Khoi dong Backend (:3000) va Frontend Vite (:5173, goi truc tiep node tranh loi ky tu '&' trong duong dan)
Start-Process powershell -WindowStyle Minimized -WorkingDirectory $BackendDir -ArgumentList "-NoProfile", "-Command", "node server.js"

$port5173 = Get-NetTCPConnection -LocalPort 5173 -State Listen -ErrorAction SilentlyContinue
if (-not $port5173) {
    Start-Process powershell -WindowStyle Minimized -WorkingDirectory $WebDir -ArgumentList "-NoProfile", "-Command", "node ./node_modules/vite/bin/vite.js --host 127.0.0.1 --port 5173"
}

# Cho ca 2 dich vu san sang phan hoi HTTP 200
$ready = $false
for ($i = 0; $i -lt 30; $i++) {
    try {
        $r1 = Invoke-WebRequest -Uri "http://localhost:3000/api/products" -UseBasicParsing -TimeoutSec 2
        $r2 = Invoke-WebRequest -Uri "http://localhost:5173/" -UseBasicParsing -TimeoutSec 2
        if ($r1.StatusCode -eq 200 -and $r2.StatusCode -eq 200) {
            $ready = $true
            break
        }
    } catch {}
    Start-Sleep -Milliseconds 500
}
if (-not $ready) {
    Write-Warning "Chua nhan duoc phan hoi day du tu cong 3000/5173 sau 15 giay — hay kiem tra cua so thu nho."
} else {
    Write-Host "[2/4] Backend (:3000, DB moi) va Frontend (:5173) da san sang." -ForegroundColor Green
}

# 4. Mo cong cu Bam gio & Thu phieu SUS cho Dieu phoi vien
$helperUri = ([System.Uri]$HelperFile).AbsoluteUri + "?session=$Session"
Start-Process $helperUri
Write-Host "[3/4] Da mo trang Bam gio & Phieu SUS: session_helper.html?session=$Session" -ForegroundColor Green

# 5. Mo cua so Google Chrome An danh moi tinh tai http://localhost:5173/ cho Nguoi tham gia
$chromePaths = @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LocalAppData\Google\Chrome\Application\chrome.exe"
)
$chromeExe = $chromePaths | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($chromeExe) {
    Start-Process -FilePath $chromeExe -ArgumentList "--incognito", "--new-window", "http://localhost:5173/"
    Write-Host "[4/4] Da mo cua so Google Chrome An danh moi tai http://localhost:5173/." -ForegroundColor Green
} else {
    Start-Process "http://localhost:5173/"
    Write-Host "[4/4] Da mo http://localhost:5173/ tren trinh duyet mac dinh." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "HUONG DAN NHANH:" -ForegroundColor Yellow
Write-Host "  1. Chon cua so Chrome An danh (EShop) -> Nhan Win + Alt + R de bat dau quay cua so."
Write-Host "  2. Bam [Bat dau / Tiep tuc] tren session_helper.html ngay khi nguoi tham gia bat dau thao tac."
Write-Host "  3. Xong nhiem vu -> Nhan Win + Alt + R dung quay -> Nguoi tham gia dien SEQ + 10 cau SUS + 4 cau mo -> Tai S0x.json."
