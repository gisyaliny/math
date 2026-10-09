@echo off
setlocal EnableExtensions
pushd "%~dp0"

REM (Optional) auto-activate a local venv if it exists
if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"

if exist ".venv\Scripts\jb.exe" (
  echo [1/2] .venv\Scripts\jb.exe build .
  ".venv\Scripts\jb.exe" build .
) else (
  where.exe jb >nul 2>nul
  if errorlevel 1 (
    echo [FAILED] Jupyter Book 1 CLI was not found.
    echo Install the project dependencies with:
    echo   .venv\Scripts\python.exe -m pip install -r requirements.txt
    goto :PAUSE
  )
  echo [1/2] jb build .
  jb build .
)
if errorlevel 1 (
  echo.
  echo [FAILED] Jupyter Book build returned %errorlevel%.
  echo.
  goto :PAUSE
)

echo.
echo [2/2] ghp-import -n -p -f _build\html
python publish.py

echo.
echo [OK] Done.

:PAUSE
echo.
echo Press any key to close...
pause >nul

popd
endlocal
