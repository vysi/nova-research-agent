# 🚀 Quick Start Guide

Get Nova Research Agent running in 5 minutes!

## Step 1: Prerequisites

Make sure you have:
- ✅ Python 3.9 or higher
- ✅ AWS Account
- ✅ Amazon Bedrock access enabled
- ✅ Nova model access (request in AWS Console if needed)

## Step 2: Install

```bash
# Clone the repo
git clone <your-repo-url>
cd nova-research-agent

# Run the setup script
./setup.sh

# Or manually:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 3: Configure AWS

1. Create a `.env` file:
```bash
cp .env.example .env
```

2. Edit `.env` with your AWS credentials:
```
AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_secret_here
AWS_REGION=us-east-1
```

### Getting AWS Credentials

1. Go to AWS Console → IAM
2. Create a new user or use existing
3. Attach policy: `AmazonBedrockFullAccess`
4. Create access key
5. Copy credentials to `.env`

### Enabling Nova Access

1. Go to AWS Console → Bedrock
2. Navigate to "Model access"
3. Request access to "Amazon Nova Pro" and "Amazon Nova Lite"
4. Wait for approval (usually instant)

## Step 4: Test Setup

```bash
python test_setup.py
```

You should see all green checkmarks ✅

## Step 5: Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Step 6: Try Your First Research

1. Enter a question like: "What are the latest developments in quantum computing?"
2. Click "🚀 Research"
3. Wait for sources to be gathered and analyzed
4. View your comprehensive research summary!

## Troubleshooting

### "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "AWS credentials not found"
- Make sure `.env` file exists
- Check that credentials are correct
- Verify no extra spaces in `.env`

### "Access denied to Nova model"
- Go to AWS Bedrock console
- Request model access
- Wait for approval

### "No sources found"
- Check your internet connection
- Try a different research query
- Some queries may not return results

## Next Steps

- Read [DEMO.md](DEMO.md) for demo tips
- Check [README.md](README.md) for full documentation
- See [DEVPOST.md](DEVPOST.md) for project details

## Need Help?

Open an issue on GitHub or check the documentation!

Happy researching! 🔬
