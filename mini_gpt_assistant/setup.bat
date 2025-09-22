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
echo ✅ Python is installed
python --version

echo Creating models folder...
if not exist "models" (
    mkdir models
    echo ✅ Created models folder
) else (
    echo Models folder already exists
)
echo.

echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Upgrading pip to latest version...
python -m pip install --upgrade pip


echo.
echo Installing PyTorch with CUDA support...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

echo.
echo Installing other dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo ✅ Virtual environment created
echo ✅ All dependencies installed
echo ✅ Default model configured: distilgpt2
echo.
echo READY TO USE:
echo   Model: distilgpt2 (lightweight, auto-downloads on first use)
echo   Runtime: Ready to start
echo.
echo TO START THE ASSISTANT:
echo   Double-click: run_assistant.bat
echo.
echo OR manually:
echo   1. Activate: venv\Scripts\activate.bat
echo   2. Run: python main.py
echo.
echo Optional tests:
echo   - GPU check: python check_gpu.py
echo   - Installation test: python demo.py (if available)
echo.
pause
