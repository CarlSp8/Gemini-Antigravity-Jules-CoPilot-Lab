@echo off
echo ================================================================
echo      Gemini AI Studio - Localhost Deployment Script
echo ================================================================
echo.

REM Check if .env exists
if not exist .env (
    echo Warning: .env file not found. Creating from .env.example...
    copy .env.example .env
    echo Done: .env file created
    echo.
    echo IMPORTANT: Please edit .env and add your Gemini API key!
    echo Get your API key from: https://aistudio.google.com/app/apikey
    echo.
    pause
)

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    echo Done: Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo Done: Dependencies installed

echo.
echo Starting Gemini AI Studio...
echo.

REM Run the application
python app.py
