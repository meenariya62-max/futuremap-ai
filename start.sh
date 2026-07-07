#!/bin/bash

echo ""
echo "============================================="
echo "  🗺️  FutureMap AI - Career Platform"
echo "============================================="
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt --quiet
echo "✅ Dependencies installed!"
echo ""

# Train model if not exists
if [ ! -f "backend/career_model.pkl" ]; then
    echo "🤖 Training ML Model... (first time only)"
    cd model_training
    python train_model.py
    cd ..
    echo "✅ Model trained!"
    echo ""
fi

# Start Flask backend
echo "🚀 Starting Flask Backend on port 5000..."
cd backend
python app.py &
cd ..

sleep 2

# Open frontend
echo "🌐 Opening Frontend..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    open frontend/login.html
else
    xdg-open frontend/login.html
fi

echo ""
echo "============================================="
echo "  ✅ FutureMap AI is Running!"
echo "  Backend : http://localhost:5000"
echo "  Frontend: frontend/login.html"
echo "============================================="
