# 🏗️ Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                      (Streamlit Web App)                     │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                 │
│  │   New    │  │ Results  │  │   Q&A    │                 │
│  │ Research │  │   View   │  │   Tab    │                 │
│  └──────────┘  └──────────┘  └──────────┘                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│                        (app.py)                             │
│                                                              │
│  • Session State Management                                 │
│  • User Input Processing                                    │
│  • Progress Tracking                                        │
│  • Export Functionality                                     │
└────────────┬──────────────────────────┬─────────────────────┘
             │                          │
             ▼                          ▼
┌────────────────────────┐  ┌──────────────────────────────┐
│   Research Engine      │  │      Nova Client             │
│  (research_engine.py)  │  │    (nova_client.py)          │
│                        │  │                              │
│  • Web Search          │  │  • Bedrock Integration       │
│  • Content Fetching    │  │  • Prompt Engineering        │
│  • Text Extraction     │  │  • Response Processing       │
│  • Source Management   │  │  • Model Selection           │
└────────┬───────────────┘  └──────────┬───────────────────┘
         │                              │
         ▼                              ▼
┌────────────────────┐      ┌──────────────────────────────┐
│  DuckDuckGo Search │      │      Amazon Bedrock          │
│        API         │      │                              │
│                    │      │  ┌────────────────────────┐  │
│  • Query Execution │      │  │   Amazon Nova Pro      │  │
│  • Result Ranking  │      │  │  (Synthesis & Analysis)│  │
│  • Metadata        │      │  └────────────────────────┘  │
└────────┬───────────┘      │                              │
         │                  │  ┌────────────────────────┐  │
         ▼                  │  │   Amazon Nova Lite     │  │
┌────────────────────┐      │  │  (Fast Responses)      │  │
│   Web Sources      │      │  └────────────────────────┘  │
│                    │      └──────────────────────────────┘
│  • Articles        │
│  • Documentation   │
│  • News Sites      │
│  • Blogs           │
└────────────────────┘
```

## Component Details

### 1. User Interface (Streamlit)

**Responsibilities:**
- Render interactive web interface
- Handle user input and interactions
- Display research results and progress
- Manage navigation between tabs
- Provide export functionality

**Key Features:**
- Real-time progress updates
- Expandable source details
- Interactive Q&A interface
- Download buttons for exports
- Research history tracking

### 2. Application Layer (app.py)

**Responsibilities:**
- Coordinate between UI and backend services
- Manage application state
- Handle user sessions
- Process and format data for display
- Implement business logic

**State Management:**
- `research_history`: List of past research queries
- `current_research`: Active research data
- `nova_client`: Singleton Nova client instance
- `research_engine`: Singleton research engine instance

### 3. Research Engine (research_engine.py)

**Responsibilities:**
- Execute web searches
- Fetch content from URLs
- Extract and clean text
- Manage source metadata
- Handle rate limiting

**Key Methods:**
- `search_web()`: Query DuckDuckGo for sources
- `fetch_content()`: Retrieve and parse web pages
- `gather_research()`: Orchestrate full research pipeline

**Technologies:**
- DuckDuckGo Search API
- BeautifulSoup4 for HTML parsing
- Requests for HTTP operations

### 4. Nova Client (nova_client.py)

**Responsibilities:**
- Interface with Amazon Bedrock
- Manage Nova model interactions
- Implement prompt engineering
- Process model responses
- Handle API errors

**Key Methods:**
- `generate_text()`: Generic text generation
- `summarize_content()`: Single-source summarization
- `synthesize_research()`: Multi-source synthesis
- `answer_question()`: Context-aware Q&A

**Model Usage:**
- **Nova Pro**: Complex synthesis, multi-source analysis
- **Nova Lite**: Quick responses, simple tasks

### 5. Configuration (config.py)

**Responsibilities:**
- Load environment variables
- Define model configurations
- Set application constants
- Manage AWS credentials

## Data Flow

### Research Query Flow

```
1. User enters query
   ↓
2. Research Engine searches web
   ↓
3. Multiple sources fetched in parallel
   ↓
4. Content extracted and cleaned
   ↓
5. Sources passed to Nova Client
   ↓
6. Nova Pro synthesizes information
   ↓
7. Results displayed to user
   ↓
8. User can ask follow-up questions
   ↓
9. Nova answers using context
```

### Question Answering Flow

```
1. User asks question
   ↓
2. Current research context retrieved
   ↓
3. Question + context sent to Nova
   ↓
4. Nova generates contextual answer
   ↓
5. Answer displayed to user
```

## API Integration

### Amazon Bedrock/Nova

**Endpoint:** `bedrock-runtime.{region}.amazonaws.com`

**Authentication:** AWS IAM credentials

**API Method:** `converse()`

**Request Format:**
```python
{
    "modelId": "us.amazon.nova-pro-v1:0",
    "messages": [
        {
            "role": "user",
            "content": [{"text": "prompt"}]
        }
    ],
    "inferenceConfig": {
        "max_new_tokens": 2000,
        "temperature": 0.7
    }
}
```

**Response Format:**
```python
{
    "output": {
        "message": {
            "content": [
                {"text": "generated response"}
            ]
        }
    }
}
```

### DuckDuckGo Search

**Library:** `duckduckgo-search`

**Method:** `DDGS().text()`

**Parameters:**
- `query`: Search terms
- `max_results`: Number of results

**Returns:** List of search results with title, URL, snippet

## Security Considerations

### Credentials Management
- AWS credentials stored in `.env` file
- Never committed to version control
- Loaded via `python-dotenv`

### API Security
- All AWS API calls use IAM authentication
- HTTPS for all external requests
- Rate limiting to prevent abuse

### Data Privacy
- No user data stored on external servers
- Research cache stored locally
- No telemetry or tracking

## Performance Optimization

### Caching Strategy
- Local research cache directory
- Prevents redundant API calls
- Speeds up repeated queries

### Parallel Processing
- Multiple sources fetched concurrently
- Reduces total research time
- Respects rate limits

### Model Selection
- Nova Pro for complex synthesis
- Nova Lite for simple tasks
- Balances quality and speed

## Error Handling

### Network Errors
- Graceful degradation when sources unavailable
- Retry logic for transient failures
- User-friendly error messages

### API Errors
- Catch and log Bedrock exceptions
- Fallback to cached results when possible
- Clear error reporting to users

### Content Errors
- Handle malformed HTML
- Skip sources that fail to parse
- Continue with available sources

## Scalability

### Current Limitations
- Single-user application
- Local state management
- Sequential research queries

### Future Scalability
- Multi-user support with database
- Distributed caching (Redis)
- Async processing with queues
- Horizontal scaling with load balancer

## Monitoring & Logging

### Current Implementation
- Console logging for debugging
- Error tracking in UI
- Basic performance metrics

### Future Enhancements
- CloudWatch integration
- Detailed performance analytics
- User behavior tracking
- Cost monitoring for API usage

## Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Docker Deployment
```dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
```

### AWS Deployment
- EC2 instance with Streamlit
- ECS container service
- Lambda + API Gateway (with modifications)
- Elastic Beanstalk

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Streamlit | Interactive UI |
| Backend | Python 3.9+ | Application logic |
| AI/ML | Amazon Nova (Bedrock) | Text generation & synthesis |
| Search | DuckDuckGo API | Web search |
| Parsing | BeautifulSoup4 | HTML extraction |
| HTTP | Requests | Web fetching |
| Config | python-dotenv | Environment management |
| AWS SDK | Boto3 | Bedrock integration |

## Future Architecture Enhancements

1. **Microservices**: Split into separate services for search, analysis, and UI
2. **Message Queue**: Add RabbitMQ/SQS for async processing
3. **Database**: PostgreSQL for persistent storage
4. **Cache Layer**: Redis for distributed caching
5. **API Gateway**: RESTful API for programmatic access
6. **Authentication**: User accounts and API keys
7. **Monitoring**: CloudWatch, Datadog, or similar
8. **CI/CD**: Automated testing and deployment
