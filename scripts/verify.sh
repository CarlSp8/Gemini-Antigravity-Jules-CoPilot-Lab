#!/bin/bash
# Quick verification script for the Spark + Gemini AI setup

echo "======================================"
echo "Spark + Gemini AI Setup Verification"
echo "======================================"
echo ""

# Check if containers are running
echo "Checking Docker containers..."
if docker ps | grep -q "spark-master"; then
    echo "✓ Spark Master is running"
else
    echo "✗ Spark Master is not running"
    echo "  Run: docker compose up -d"
    exit 1
fi

if docker ps | grep -q "spark-worker"; then
    echo "✓ Spark Worker is running"
else
    echo "✗ Spark Worker is not running"
fi

if docker ps | grep -q "jupyter-spark"; then
    echo "✓ Jupyter is running"
else
    echo "✗ Jupyter is not running"
fi

echo ""
echo "Checking service endpoints..."

# Check Spark Master UI
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8080 | grep -q "200"; then
    echo "✓ Spark Master UI: http://localhost:8080"
else
    echo "✗ Spark Master UI not accessible"
fi

# Check Spark Worker UI
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8081 | grep -q "200"; then
    echo "✓ Spark Worker UI: http://localhost:8081"
else
    echo "✗ Spark Worker UI not accessible"
fi

# Check Jupyter
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8888 | grep -q "200\|302"; then
    echo "✓ Jupyter Lab: http://localhost:8888"
else
    echo "✗ Jupyter Lab not accessible"
fi

echo ""
echo "Checking configuration..."

if [ -f .env ]; then
    echo "✓ .env file exists"
    
    if grep -q "GOOGLE_AI_API_KEY=your-api-key-here" .env; then
        echo "! Google AI API Key not configured (optional)"
        echo "  Get your key from: https://aistudio.google.com/"
    else
        echo "✓ Google AI API Key configured"
    fi
else
    echo "✗ .env file not found"
    echo "  Run: cp .env.example .env"
fi

echo ""
echo "======================================"
echo "Project structure:"
echo "======================================"
tree -L 2 -I '.git' . 2>/dev/null || find . -maxdepth 2 -not -path '*/\.git/*' -not -path './.git' | head -20

echo ""
echo "======================================"
echo "Verification complete!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Open Jupyter Lab: http://localhost:8888"
echo "2. Try the demo notebook: notebooks/spark_gemini_demo.ipynb"
echo "3. Run example script: docker exec -it jupyter-spark python /home/jovyan/scripts/spark_gemini_example.py"
echo ""
