@echo off
REM Quick launcher for Mini GPT Assistant

echo Starting Mini GPT Assistant...
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first to create the environment.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if config.py has a valid model name
findstr /C:"MODEL_NAME = \"PLACEHOLDER\"" config.py >nul
if not errorlevel 1 (
    echo ERROR: No model configured!
    echo.
    echo You MUST change the PLACEHOLDER in config.py first!
    echo.
    echo REQUIRED STEPS:
    echo 1. Open config.py in Notepad
    echo.
    echo 2. Find this line:
    echo    MODEL_NAME = "PLACEHOLDER"
    echo.
    echo 3. Change it to one of these recommended models:
    echo    MODEL_NAME = "distilgpt2"              # Lightweight, good for beginners
    echo    MODEL_NAME = "gpt2"                    # Standard GPT-2 model
    echo    MODEL_NAME = "microsoft/DialoGPT-medium"  # Good for conversations
    echo.
    echo 4. Save config.py and run this script again
    echo.
    echo The model will auto-download on first use (requires internet)
    echo.
    echo For beginners, we recommend: MODEL_NAME = "distilgpt2"
    echo.
    pause
    exit /b 1
)

echo.
echo Model configured successfully! Starting assistant...
echo.

REM Run the assistant with error handling
python main.py
if errorlevel 1 (
    echo.
    echo ERROR: Assistant failed to start!
    echo.
    echo Common solutions:
    echo 1. If you get "model not found" error:
    echo    - Download a model from https://huggingface.co/models
    echo    - Update MODEL_NAME in config.py to match your model exactly
    echo    - For auto-download, use: MODEL_NAME = "distilgpt2"
    echo.
    echo 2. If you get "out of memory" error:
    echo    - Use a smaller model like "distilgpt2"
    echo    - Set USE_GPU = False in config.py to use CPU
    echo    - Close other applications to free RAM
    echo.
    echo 3. If you get "import" errors:
    echo    - Run: pip install -r requirements.txt
    echo    - Make sure virtual environment is activated
    echo.
    echo 4. If you get GPU/CUDA errors:
    echo    - Run: python check_gpu.py (to diagnose GPU issues)
    echo    - Set USE_GPU = False in config.py to use CPU instead
    echo.
    echo Check logs/assistant.log for detailed error information.
    echo.
)

echo.
echo Assistant ended. Press any key to close...
pause >nul
