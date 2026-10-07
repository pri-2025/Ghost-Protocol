@echo off
echo ====================================================================
echo       CITI DRUNIX HACKATHON: PROJECT GHOST PROTOCOL (LAUNCHER)
echo ====================================================================
echo Starting all microservices in separate consoles...

start "Sentinel FastAPI Engine (:8000)" cmd /c "run_sentinel.bat"
timeout /t 2 /nobreak >nul

start "Core Banking Spring Boot (:8080)" cmd /c "run_banking.bat"
timeout /t 3 /nobreak >nul

start "Security Operations Console (Streamlit)" cmd /c "run_dashboard.bat"

echo All services dispatched! Open browser at http://localhost:8501
pause
