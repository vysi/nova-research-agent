# Nova Research Agent

AI-powered research assistant using Amazon Nova to gather, analyze, and synthesize information from multiple sources.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)
![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎬 Demo Video

Watch the demo: [Nova Research Agent Demo](https://www.loom.com/share/ee0581efc8ff4a1a8ac0c0241e1de505)

## Overview

Transform hours of manual research into seconds with AI-powered intelligence. Nova Research Agent automatically searches multiple sources, analyzes content, and generates comprehensive research summaries with citations.

## Features

- Multi-source web search and aggregation
- AI-powered synthesis using Amazon Nova
- Automated insight extraction
- Interactive visualizations and analytics
- Q&A interface with conversation history
- Export to JSON, Text, and Markdown formats
- Real-time progress tracking
- Source relevance scoring

## Quick Start

```bash
# Install dependencies
./setup.sh

# Configure AWS credentials
cp .env.example .env
# Edit .env with your AWS credentials

# Run application
streamlit run app.py
```

See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.

## Technology Stack

- **Amazon Nova AI** - Language models for synthesis and analysis
- **Amazon Bedrock** - Managed AI service
- **Streamlit** - Web application framework
- **Python 3.9+** - Core programming language
- **Plotly** - Interactive visualizations
- **DuckDuckGo Search** - Web search API
- **BeautifulSoup4** - Content extraction

## Project Structure

```
nova-research-agent/
├── app.py                 # Main application
├── nova_client.py         # Amazon Nova integration
├── research_engine.py     # Web search and extraction
├── utils.py              # Utility functions
├── demo_mode.py          # Demo mode support
├── config.py             # Configuration
├── requirements.txt      # Dependencies
└── README.md            # Documentation
```

## Documentation

- [QUICKSTART.md](QUICKSTART.md) - Quick setup guide
- [ARCHITECTURE.md](ARCHITECTURE.md) - Technical architecture
- [FEATURE_SHOWCASE.md](FEATURE_SHOWCASE.md) - Complete feature list
- [DEVPOST.md](DEVPOST.md) - Hackathon submission details

## License

MIT License - See [LICENSE](LICENSE) for details

## Built For

Amazon Nova AI Hackathon 2026
