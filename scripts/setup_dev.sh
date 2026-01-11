#!/bin/bash
set -e

echo "🚀 Setting up development environment..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet
pip install -r requirements-dev.txt --quiet
echo "✓ Dependencies installed"

# Install pre-commit hooks
if command -v pre-commit &> /dev/null; then
    echo "Installing pre-commit hooks..."
    pre-commit install
    echo "✓ Pre-commit hooks installed"
else
    echo "⚠️  pre-commit not found, skipping hooks installation"
fi

# Copy environment template
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file - please update with your credentials"
else
    echo "✓ .env file already exists"
fi

# Generate secret keys
echo ""
echo "🔐 Generate secret keys with:"
echo "  SECRET_KEY: openssl rand -hex 32"
echo "  ENCRYPTION_KEY: openssl rand -hex 32"
echo ""
echo "Update these in your .env file"
echo ""

echo "✅ Development environment ready!"
echo ""
echo "Next steps:"
echo "  1. source venv/bin/activate"
echo "  2. Update .env with your credentials"
echo "  3. uvicorn src.main:app --reload"
echo ""
