"""
Demo Mode - For testing without AWS credentials
Provides mock responses to simulate Nova AI
"""

DEMO_RESPONSES = {
    "quantum computing": """
    # Quantum Computing Research Summary

    Recent developments in quantum computing have shown significant progress across multiple fronts [Source 1][Source 2].

    ## Key Developments

    **Hardware Advances**: Major tech companies have achieved new milestones in qubit stability and error correction [Source 1]. IBM's latest quantum processor demonstrates improved coherence times, while Google's quantum AI team has made breakthroughs in quantum error correction [Source 3].

    **Practical Applications**: Quantum computing is moving beyond theoretical research into practical applications [Source 2]. Financial institutions are exploring quantum algorithms for portfolio optimization, while pharmaceutical companies are using quantum simulations for drug discovery [Source 4].

    **Challenges**: Despite progress, significant challenges remain [Source 5]. Maintaining quantum coherence at scale, reducing error rates, and developing quantum-resistant cryptography are ongoing concerns.

    ## Future Outlook

    Experts predict that quantum advantage for specific commercial applications could be achieved within the next 3-5 years [Source 3]. However, general-purpose quantum computers remain a longer-term goal.
    """,
    
    "artificial intelligence": """
    # Artificial Intelligence Research Summary

    The AI landscape in 2026 continues to evolve rapidly with several key trends emerging [Source 1][Source 2].

    ## Major Trends

    **Large Language Models**: Advanced language models have become more efficient and capable [Source 1]. New architectures reduce computational requirements while improving performance on complex reasoning tasks [Source 3].

    **AI Safety and Ethics**: Growing focus on responsible AI development [Source 2]. Organizations are implementing frameworks for AI governance, bias detection, and transparency [Source 4].

    **Multimodal AI**: Integration of text, image, and video understanding in single models [Source 3]. This enables more natural human-AI interaction and broader application possibilities [Source 5].

    ## Industry Impact

    AI adoption across industries has accelerated, with healthcare, finance, and education seeing particularly significant transformations [Source 4]. However, concerns about job displacement and AI regulation continue to be debated [Source 5].
    """,
    
    "default": """
    # Research Summary

    Based on analysis of multiple sources, here are the key findings [Source 1][Source 2].

    ## Main Points

    The research reveals several important aspects of this topic [Source 1]. Current developments show promising trends, though challenges remain [Source 2].

    **Key Finding 1**: Significant progress has been made in recent years [Source 3]. Multiple studies confirm this trend across different contexts [Source 4].

    **Key Finding 2**: Experts emphasize the importance of continued research and development [Source 2]. Future directions include expanded applications and improved methodologies [Source 5].

    ## Implications

    These findings have important implications for both theory and practice [Source 3]. Stakeholders should consider these developments when planning future initiatives [Source 4].

    ## Conclusion

    While progress is evident, ongoing research is needed to address remaining questions and challenges [Source 5].
    """
}

DEMO_SOURCES = [
    {
        'title': 'Recent Advances in the Field - Nature Journal',
        'url': 'https://nature.com/articles/example-1',
        'snippet': 'Comprehensive overview of recent developments and breakthrough discoveries in the field.',
        'content': 'Detailed analysis of recent advances... ' * 50
    },
    {
        'title': 'Industry Report 2026 - Tech Research Institute',
        'url': 'https://techresearch.org/reports/2026',
        'snippet': 'Annual industry report covering trends, statistics, and future predictions.',
        'content': 'Industry analysis and market trends... ' * 50
    },
    {
        'title': 'Expert Analysis - Scientific American',
        'url': 'https://scientificamerican.com/article/expert-analysis',
        'snippet': 'Expert perspectives on current challenges and opportunities in the field.',
        'content': 'Expert commentary and analysis... ' * 50
    },
    {
        'title': 'Practical Applications - MIT Technology Review',
        'url': 'https://technologyreview.com/practical-applications',
        'snippet': 'Real-world applications and case studies demonstrating practical impact.',
        'content': 'Case studies and practical examples... ' * 50
    },
    {
        'title': 'Future Outlook - Forbes Technology',
        'url': 'https://forbes.com/technology/future-outlook',
        'snippet': 'Forward-looking analysis of future trends and potential developments.',
        'content': 'Future predictions and analysis... ' * 50
    }
]

DEMO_INSIGHTS = """
1. Significant technological progress has been achieved in recent years
2. Multiple practical applications are now emerging in various industries
3. Key challenges remain around scalability and implementation
4. Expert consensus points to continued growth and development
5. Future outlook remains positive with several promising directions
"""


def get_demo_synthesis(query: str) -> str:
    """Get demo synthesis based on query"""
    query_lower = query.lower()
    
    if "quantum" in query_lower:
        return DEMO_RESPONSES["quantum computing"]
    elif "ai" in query_lower or "artificial intelligence" in query_lower:
        return DEMO_RESPONSES["artificial intelligence"]
    else:
        return DEMO_RESPONSES["default"]


def get_demo_sources() -> list:
    """Get demo sources"""
    return DEMO_SOURCES


def get_demo_insights() -> str:
    """Get demo insights"""
    return DEMO_INSIGHTS


def is_demo_mode() -> bool:
    """Check if running in demo mode (no AWS credentials)"""
    import os
    aws_key = os.getenv("AWS_ACCESS_KEY_ID")
    return not aws_key or aws_key == "your_access_key_here" or aws_key == "DEMO_MODE"
