@echo off
title FutureMap AI - Launcher
color 0A
echo.
echo  =============================================
echo   FutureMap AI - Career Platform
echo  =============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python not found! Install Python first.
    pause
    exit
)

echo  Installing dependencies...
pip install flask flask-cors scikit-learn pandas numpy joblib --only-binary=:all: --quiet
echo  Dependencies ready!
echo.

if not exist "backend\career_model.pkl" (
    echo  Training ML Model...
    cd model_training
    python train_model.py
    cd ..
    echo  Model trained!
    echo.
)

echo  Starting Backend...
start "FutureMap Backend" cmd /k "cd backend && python app.py"
timeout /t 2 /nobreak >nul

echo  Opening in Browser...
start "" "http://127.0.0.1:5000"

echo.
echo  FutureMap AI is Running!
echo  Open: http://127.0.0.1:5000
echo.
pause
