@echo off
REM Quick launcher for Mini GPT Assistant

echo Starting Mini GPT Assistant...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the assistant
python main.py

echo.
echo Assistant ended. Press any key to close...
pause >nul
