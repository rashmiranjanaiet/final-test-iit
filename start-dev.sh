#!/bin/bash
# Linux/macOS startup script for local development

echo ""
echo "============================================"
echo "  Causal Chat Analysis - Flask App"
echo "============================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Install with: brew install python3  (macOS) or apt-get install python3 (Linux)"
    exit 1
fi

# Create venv if needed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -q -r requirements-prod.txt

# Create .env if needed
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env with your settings"
fi

# Run app
echo ""
echo "Starting Flask application..."
echo ""
echo "Application running at: http://localhost:5000"
echo "Press Ctrl+C to stop"
echo ""

python wsgi.py
