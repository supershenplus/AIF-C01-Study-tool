@echo off
echo Setting up AWS AI Practitioner Study Tool...
echo.

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt -q

echo.
echo Setup complete! Run the tool with:
echo   python -m aws_ai_study.main
echo.
