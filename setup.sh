#!/bin/bash

echo "🔬 Setting up Nova Research Agent..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Please edit .env file with your AWS credentials"
fi

echo "✅ Setup complete!"
echo "📝 Next steps:"
echo "   1. Edit .env file with your AWS credentials"
echo "   2. Run: source venv/bin/activate"
echo "   3. Run: streamlit run app.py"
