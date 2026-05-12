@echo off
cd /d "%~dp0"
call venv\Scripts\activate
python -m aws_ai_study.main %*
