# Nova Research Agent - Devpost Submission

## Inspiration

Research is overwhelming. Whether you're a student writing a paper, a professional analyzing market trends, or a researcher exploring new topics, the process of gathering information from multiple sources, reading through countless articles, and synthesizing insights takes hours or even days. We built Nova Research Agent to transform this tedious, time-consuming process into an intelligent, conversational experience powered by Amazon Nova AI.

## What it does

Nova Research Agent is an AI-powered research assistant that revolutionizes how people conduct research:

- **Intelligent Multi-Source Search**: Automatically gathers relevant information from multiple web sources based on your research query
- **AI-Powered Analysis**: Uses Amazon Nova's advanced language models to deeply analyze and understand content from each source
- **Smart Synthesis**: Combines information across all sources into a comprehensive, well-structured research summary with proper citations
- **Automated Insight Extraction**: Nova automatically identifies and highlights the most important findings from your research
- **Interactive Q&A**: Answer follow-up questions about your research using Nova's contextual understanding, with full conversation history
- **Visual Analytics Dashboard**: Track your research patterns, topic trends, and activity over time with interactive charts
- **Professional Export**: Generate publication-ready research reports in multiple formats (JSON, text, Markdown)
- **Source Transparency**: Every claim is backed by citations with relevance scoring, allowing users to verify information
- **Real-time Progress Tracking**: Visual feedback showing research progress from search to synthesis
- **Smart Suggestions**: Get topic suggestions and example questions to enhance your research

Instead of spending hours manually reading through dozens of articles, users simply ask a research question and receive a comprehensive, cited summary with visual insights in seconds.

## How we built it

### Technology Stack

- **Amazon Nova AI Models**: Core intelligence using Nova Pro via Amazon Bedrock for natural language understanding, synthesis, and generation
- **Amazon Bedrock**: Managed service providing secure, scalable access to Nova models
- **Python Backend**: Core application logic and API integration
- **Streamlit**: Interactive web interface for seamless user experience
- **Plotly**: Advanced data visualizations for analytics and insights
- **DuckDuckGo Search API**: Privacy-focused web search for source discovery
- **BeautifulSoup4**: Intelligent web content extraction and cleaning
- **Boto3**: AWS SDK for Bedrock/Nova integration

### Architecture

1. **Research Engine**: Searches the web, fetches content, and extracts main text from multiple sources
2. **Nova Client**: Interfaces with Amazon Bedrock to access Nova models for:
   - Content summarization
   - Multi-source synthesis
   - Automated insight extraction
   - Question answering
   - Context-aware generation
3. **Analytics Engine**: Processes research data to generate visualizations and track patterns
4. **Streamlit UI**: Provides an intuitive 4-tab interface with:
   - New Research tab with progress tracking
   - Results & Insights tab with visualizations
   - Interactive Q&A tab with conversation history
   - Analytics dashboard with research trends

### Key Implementation Details

- **Advanced Prompt Engineering**: Carefully crafted system prompts to ensure Nova generates accurate, well-cited research summaries and extracts meaningful insights
- **Content Processing**: Intelligent text extraction that removes noise while preserving important information
- **Citation Tracking**: Maintains source attribution throughout the entire analysis pipeline
- **Visual Analytics**: Real-time charts showing source relevance, topic distribution, and research patterns
- **Session Management**: Robust state management for research history and conversation tracking
- **Error Handling**: Graceful degradation when sources are unavailable or API calls fail
- **Rate Limiting**: Respectful web scraping with appropriate delays
- **Progressive Enhancement**: Features like visualizations and analytics that enhance without blocking core functionality

## Challenges we ran into

1. **Citation Accuracy**: Ensuring that Nova's synthesized content properly attributes information to the correct sources required careful prompt engineering and output parsing

2. **Content Quality**: Web pages contain lots of noise (ads, navigation, etc.). We had to implement sophisticated content extraction to get clean, relevant text for Nova to analyze

3. **Prompt Optimization**: Finding the right balance in prompts to get comprehensive summaries without hallucination or losing important details took multiple iterations

4. **Real-time UX**: Balancing thoroughness (fetching multiple sources) with speed (keeping users engaged) required optimizing our pipeline and adding progress indicators

5. **Model Selection**: Choosing between Nova Pro (more capable but slower) and Nova Lite (faster but less nuanced) for different tasks to optimize both quality and performance

## Accomplishments that we're proud of

- **Seamless Nova Integration**: Successfully integrated Amazon Nova models to create a truly intelligent research assistant that understands context and synthesizes information like a human researcher

- **Advanced Analytics**: Built a comprehensive analytics dashboard with interactive visualizations that help users understand their research patterns and trends

- **Automated Insight Extraction**: Implemented AI-powered insight extraction that automatically identifies the most important findings from research

- **Citation Integrity**: Built a system that maintains source attribution throughout the entire pipeline, ensuring academic and professional integrity

- **Professional UX**: Created an intuitive, modern interface with 4 specialized tabs, real-time progress tracking, and celebration animations that makes advanced AI research accessible to everyone

- **Conversation Memory**: Implemented Q&A with full conversation history, allowing natural, contextual discussions about research

- **Real-World Utility**: Built something that solves a genuine problem we face daily - the tool actually saves hours of research time

- **Production Ready**: The application is robust, handles errors gracefully, includes comprehensive visualizations, and is ready for real-world use

- **Complete Package**: Not just code, but comprehensive documentation, demo materials, test scripts, and deployment guides

## What we learned

- **Nova's Capabilities**: Gained deep understanding of Amazon Nova's strengths in multi-document synthesis and contextual understanding. Nova Pro excels at maintaining coherence across long contexts.

- **Prompt Engineering**: Learned that effective prompts for research synthesis require clear instructions about citation format, objectivity, and handling conflicting information

- **AWS Bedrock**: Discovered best practices for using Bedrock's Converse API, including proper message formatting and inference configuration

- **Research Workflows**: Understanding how researchers actually work helped us design features that fit naturally into existing workflows

- **Streaming vs Batch**: Learned when to use streaming responses (for better UX) vs batch processing (for complex synthesis tasks)

## What's next for Nova Research Agent

### Short-term Enhancements
- **PDF Analysis**: Add support for uploading and analyzing PDF documents, especially academic papers
- **Streaming Responses**: Implement real-time streaming of Nova's synthesis for better user experience
- **Advanced Filtering**: Allow users to filter sources by date, domain, or credibility
- **Export Formats**: Add Markdown, PDF, and formatted citation exports (APA, MLA, Chicago)

### Medium-term Features
- **Collaborative Research**: Enable teams to share and collaborate on research projects
- **Reference Manager Integration**: Connect with Zotero, Mendeley, and EndNote
- **Custom Source Lists**: Allow users to specify trusted sources or domains
- **Research Templates**: Pre-built templates for different research types (academic, market, technical)

### Long-term Vision
- **Multi-language Support**: Research in and translate between multiple languages using Nova's multilingual capabilities
- **Visual Knowledge Graphs**: Generate interactive visualizations of research connections and relationships
- **Academic Paper Generation**: Use Nova to help draft research papers based on gathered sources
- **API Access**: Provide API for developers to integrate research capabilities into their own applications
- **Mobile App**: Native mobile experience for research on the go

### Nova-Specific Enhancements
- **Multi-modal Research**: Leverage Nova's vision capabilities to analyze charts, graphs, and images in sources
- **Fine-tuning**: Create domain-specific versions (medical research, legal research, etc.) using Nova's fine-tuning capabilities
- **Agentic Workflows**: Implement autonomous research agents that can iteratively refine queries and explore related topics

## Impact

Nova Research Agent democratizes access to high-quality research capabilities. Students can conduct literature reviews faster, professionals can make data-driven decisions quicker, and researchers can explore new domains more efficiently. By reducing research time from hours to minutes, we're enabling more people to make informed decisions based on comprehensive information.

## Try it yourself

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure AWS credentials with Bedrock/Nova access
4. Run: `streamlit run app.py`
5. Start researching!

## Built with Amazon Nova

This project showcases Amazon Nova's capabilities in:
- Long-context understanding across multiple documents
- Accurate information synthesis with citation preservation
- Contextual question answering
- Professional-quality text generation
- Consistent, reliable performance at scale

---

**Built for Amazon Nova AI Hackathon 2026**
