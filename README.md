# 🔬 Nova Research Agent

```
███╗   ██╗ ██████╗ ██╗   ██╗ █████╗     ██████╗ ███████╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
████╗  ██║██╔═══██╗██║   ██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██╔██╗ ██║██║   ██║██║   ██║███████║    ██████╔╝█████╗  ███████╗█████╗  ███████║██████╔╝██║     ███████║
██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║    ██╔══██╗██╔══╝  ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║    ██║  ██║███████╗███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
```

> 🏆 **Built for Amazon Nova AI Hackathon 2026** | ⭐ **[START HERE](START_HERE.md)** for complete guide

AI-powered research assistant using Amazon Nova to gather, analyze, and synthesize information from multiple sources. Get comprehensive, cited research summaries in seconds, not hours.

![Amazon Nova AI Hackathon](https://img.shields.io/badge/Amazon%20Nova-AI%20Hackathon%202026-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red?style=for-the-badge&logo=streamlit)
![AWS](https://img.shields.io/badge/AWS-Bedrock-orange?style=for-the-badge&logo=amazon-aws)

---

## 🚀 Quick Links

- **[📖 START HERE](START_HERE.md)** - Complete guide to winning the hackathon
- **[⚡ QUICKSTART](QUICKSTART.md)** - Get running in 5 minutes
- **[✅ SUBMISSION CHECKLIST](SUBMISSION_CHECKLIST.md)** - Step-by-step submission guide
- **[🏆 WINNING FEATURES](WINNING_FEATURES.md)** - Why this will win
- **[✨ FEATURE SHOWCASE](FEATURE_SHOWCASE.md)** - All 30+ features explained

---

## 🎯 What It Does

Nova Research Agent transforms the research process by:
- **🔍 Intelligent Search**: Automatically gathers information from multiple web sources
- **🤖 AI Analysis**: Uses Amazon Nova models to analyze and synthesize content
- **💡 Smart Insights**: Automatically extracts key findings and important information
- **📊 Visual Analytics**: Track research patterns with interactive charts and graphs
- **💬 Interactive Q&A**: Answer follow-up questions with conversation memory
- **📥 Export Ready**: Download research reports in multiple formats (JSON, Text, Markdown)
- **🎯 Citation Tracking**: Every claim backed by verifiable sources

**Result**: Research that takes hours now takes seconds, with better quality and full transparency.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- AWS Account with Bedrock access
- Amazon Nova model access enabled

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd nova-research-agent

# Run setup script
./setup.sh

# Or manual setup:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Add your AWS credentials to `.env`:
```
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1
```

3. Ensure you have Amazon Nova model access in AWS Bedrock

### Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 💡 How to Use

1. **Start Research**: Enter your research question in the "New Research" tab
2. **Review Results**: View the AI-generated synthesis and sources in the "Results" tab
3. **Ask Questions**: Use the "Q&A" tab to ask follow-up questions
4. **Export**: Download your research as JSON or text format

## 🏗️ Architecture

```
┌─────────────────┐
│   Streamlit UI  │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼──┐  ┌──▼────────┐
│ Nova │  │ Research  │
│Client│  │  Engine   │
└───┬──┘  └──┬────────┘
    │        │
    │    ┌───▼────────┐
    │    │ DuckDuckGo │
    │    │   Search   │
    │    └────────────┘
    │
┌───▼─────────────┐
│ Amazon Bedrock  │
│  (Nova Models)  │
└─────────────────┘
```

## 🔑 Key Features

### Multi-Source Research
- Automatically searches and retrieves content from multiple sources
- Extracts and cleans main content from web pages
- Respects rate limits and handles errors gracefully

### Amazon Nova Integration
- Uses Nova Pro for comprehensive research synthesis
- Implements proper prompt engineering for accurate results
- Supports multiple Nova model configurations

### Citation Tracking
- Maintains source attribution throughout analysis
- Provides clickable links to original sources
- Includes source snippets for context

### Interactive Experience
- Real-time research progress updates
- Expandable source details
- Follow-up question answering
- Research history tracking

## 📁 Project Structure

```
nova-research-agent/
├── app.py                 # Main Streamlit application
├── nova_client.py         # Amazon Nova/Bedrock client
├── research_engine.py     # Web search and content extraction
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── setup.sh             # Setup script
├── .env.example         # Environment variables template
└── README.md            # This file
```

## 🛠️ Technologies Used

- **Amazon Nova AI**: Advanced language models for synthesis and analysis
- **Amazon Bedrock**: Managed service for Nova model access
- **Streamlit**: Interactive web application framework
- **DuckDuckGo Search**: Privacy-focused web search
- **BeautifulSoup4**: Web content extraction
- **Python 3.9+**: Core programming language

## 🎓 Use Cases

- **Academic Research**: Quickly gather and synthesize academic information
- **Market Analysis**: Research market trends and competitor information
- **Technical Documentation**: Aggregate technical knowledge from multiple sources
- **News Aggregation**: Synthesize news from multiple outlets
- **Due Diligence**: Research companies, products, or technologies

## 🔒 Security & Privacy

- AWS credentials stored in local `.env` file (never committed)
- No data stored on external servers
- Research cache stored locally
- Respects robots.txt and rate limits

## 🚧 Future Enhancements

- [ ] PDF and academic paper analysis
- [ ] Collaborative research features
- [ ] Integration with reference managers (Zotero, Mendeley)
- [ ] Multi-language support
- [ ] Visual knowledge graphs
- [ ] Real-time streaming responses
- [ ] Custom source filtering

## 📝 License

MIT License - feel free to use and modify!

## 🏆 Built For

Amazon Nova AI Hackathon 2026

## 👥 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.
