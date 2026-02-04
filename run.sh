#!/bin/bash

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     Gemini AI Studio - Localhost Deployment Script       ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from .env.example..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "❗ IMPORTANT: Please edit .env and add your Gemini API key!"
    echo "   Get your API key from: https://aistudio.google.com/app/apikey"
    echo ""
    read -p "Press Enter after you've added your API key to continue..."
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

echo ""
echo "🚀 Starting Gemini AI Studio..."
echo ""

# Run the application
python app.py
