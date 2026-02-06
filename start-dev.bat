@echo off
REM Windows startup script for local development

echo.
echo ============================================
echo   Causal Chat Analysis - Flask App
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install/update dependencies
echo.
echo Installing dependencies...
pip install -q -r requirements-prod.txt

REM Create .env if it doesn't exist
if not exist ".env" (
    echo.
    echo Creating .env file from template...
    copy .env.example .env
    echo Please edit .env with your settings
)

REM Run the application
echo.
echo Starting Flask application...
echo.
echo Application running at: http://localhost:5000
echo Press Ctrl+C to stop
echo.

python wsgi.py

pause
