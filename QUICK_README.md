# 🚀 Nova Research Agent - Quick Guide

## What is This?

AI-powered research assistant that uses Amazon Nova to turn hours of research into 30 seconds.

## Quick Start (3 Steps)

### 1. Install
```bash
./setup.sh
```

### 2. Configure (Choose One)

**Option A: Demo Mode (No AWS needed)**
```bash
# Just run it!
streamlit run app.py
```
App will run in demo mode with sample data.

**Option B: Real Nova AI**
```bash
# Create .env file
cp .env.example .env

# Edit .env with your AWS credentials
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1
```

### 3. Run
```bash
streamlit run app.py
```

## Features

- 🔍 Multi-source web search
- 🤖 AI synthesis (Amazon Nova)
- 💡 Automated insights
- 📊 Visual analytics
- 💬 Interactive Q&A
- 📥 Export (JSON/Text/Markdown)

## Demo Mode vs Real Mode

| Feature | Demo Mode | Real Mode |
|---------|-----------|-----------|
| Web Search | ✅ Real | ✅ Real |
| AI Synthesis | 📝 Sample | 🤖 Nova AI |
| Visualizations | ✅ Real | ✅ Real |
| Export | ✅ Works | ✅ Works |
| AWS Required | ❌ No | ✅ Yes |

## Troubleshooting

**"No module named 'streamlit'"**
```bash
pip install -r requirements.txt
```

**"AWS credentials not found"**
- App runs in demo mode automatically
- To use real Nova: Add credentials to .env

**"No sources found"**
- Check internet connection
- Try different query

## Files

- `app.py` - Main application
- `nova_client.py` - Nova AI integration
- `research_engine.py` - Web search
- `utils.py` - Helper functions
- `demo_mode.py` - Demo mode support

## For Hackathon Submission

1. Test in demo mode first
2. Get AWS credentials
3. Test with real Nova
4. Take screenshots
5. Record video
6. Submit!

See `START_HERE.md` for complete guide.

## Need Help?

- Demo mode issues: Check internet connection
- AWS issues: See QUICKSTART.md
- Features: See FEATURE_SHOWCASE.md
- Submission: See SUBMISSION_CHECKLIST.md

---

**Built for Amazon Nova AI Hackathon 2026** 🏆
