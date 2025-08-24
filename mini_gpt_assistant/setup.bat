@echo off
REM Mini GPT Assistant - Windows Setup Script
REM This script sets up the Python environment and installs dependencies

echo.
echo ========================================
echo Mini GPT Assistant - Windows Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11 or higher from https://python.org and add it to PATH
    pause
    exit /b 1
)

echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Running installation test...
python demo.py

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the assistant:
echo   1. Activate the virtual environment: venv\Scripts\activate.bat
echo   2. Run the assistant: python main.py
echo.
echo Or simply double-click 'run_assistant.bat'
echo.
pause
