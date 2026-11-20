# Run from the repository root after installing Ruff and Pylint.
$target = "week5/legacy_fees.py"
$output = @()
$output += "=== ruff check $target ==="
$output += (ruff check $target 2>&1 | Out-String)
$output += "=== ruff check $target --statistics ==="
$output += (ruff check $target --statistics 2>&1 | Out-String)
$output += "=== pylint $target ==="
$output += (pylint $target 2>&1 | Out-String)
$output | Set-Content -Encoding utf8 "docs/week5/before.txt"
Write-Host "Saved actual Ruff and Pylint output to docs/week5/before.txt"
