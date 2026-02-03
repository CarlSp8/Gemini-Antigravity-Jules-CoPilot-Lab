#!/bin/bash
# Setup script for local Spark environment with Copilot Pro+ toolkit

set -e

echo "======================================"
echo "Spark + Gemini AI Home Lab Setup"
echo "======================================"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

echo "✓ Docker is installed"

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✓ Docker Compose is available"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit the .env file and add your configuration:"
    echo "   - Set JUPYTER_TOKEN for Jupyter notebook access"
    echo "   - Set GOOGLE_AI_API_KEY from https://aistudio.google.com/"
else
    echo "✓ .env file already exists"
fi

# Create required directories
echo ""
echo "Setting up directories..."
mkdir -p data notebooks scripts
echo "✓ Directories created"

# Pull Docker images
echo ""
echo "Pulling Docker images (this may take a few minutes)..."
docker-compose pull

echo ""
echo "======================================"
echo "✓ Setup Complete!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your API keys and tokens"
echo "2. Start the environment: docker-compose up -d"
echo "3. Access the services:"
echo "   - Spark Master UI: http://localhost:8080"
echo "   - Spark Worker UI: http://localhost:8081"
echo "   - Jupyter Lab: http://localhost:8888"
echo ""
echo "4. Check logs: docker-compose logs -f"
echo "5. Stop services: docker-compose down"
echo ""
echo "For more information, see README.md"
