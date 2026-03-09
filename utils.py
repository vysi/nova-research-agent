"""
Utility functions for Nova Research Agent
"""
import re
from collections import Counter
from typing import List, Dict
import hashlib


def calculate_source_relevance(source: Dict, query: str) -> float:
    """
    Calculate relevance score for a source based on query
    Returns score between 0-100
    """
    score = 50.0  # Base score
    
    query_words = set(query.lower().split())
    
    # Check title relevance
    title = source.get('title', '').lower()
    title_words = set(title.split())
    title_overlap = len(query_words.intersection(title_words))
    score += title_overlap * 10
    
    # Check snippet relevance
    snippet = source.get('snippet', '').lower()
    snippet_words = set(snippet.split())
    snippet_overlap = len(query_words.intersection(snippet_words))
    score += snippet_overlap * 5
    
    # Check content length (longer = more comprehensive)
    content_length = len(source.get('content', ''))
    if content_length > 3000:
        score += 10
    elif content_length > 1000:
        score += 5
    
    # URL credibility (simple heuristic)
    url = source.get('url', '').lower()
    credible_domains = ['.edu', '.gov', '.org', 'wikipedia', 'arxiv', 'nature', 'science']
    if any(domain in url for domain in credible_domains):
        score += 15
    
    # Cap at 100
    return min(score, 100.0)


def extract_key_terms(text: str, top_n: int = 10) -> Dict[str, int]:
    """
    Extract key terms from text using frequency analysis
    """
    # Remove common stop words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
        'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that',
        'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
        'what', 'which', 'who', 'when', 'where', 'why', 'how'
    }
    
    # Extract words
    words = re.findall(r'\b[a-z]{4,}\b', text.lower())
    
    # Filter stop words
    filtered_words = [w for w in words if w not in stop_words]
    
    # Count frequency
    word_freq = Counter(filtered_words)
    
    return dict(word_freq.most_common(top_n))


def generate_source_id(url: str) -> str:
    """
    Generate unique ID for a source based on URL
    """
    return hashlib.md5(url.encode()).hexdigest()[:8]


def format_citation(source_num: int, title: str, url: str) -> str:
    """
    Format a citation in a standard way
    """
    return f"[{source_num}] {title}. Retrieved from {url}"


def estimate_reading_time(text: str) -> int:
    """
    Estimate reading time in minutes (assuming 200 words/min)
    """
    word_count = len(text.split())
    return max(1, round(word_count / 200))


def calculate_synthesis_quality(synthesis: str, sources: List[Dict]) -> Dict:
    """
    Calculate quality metrics for synthesis
    """
    # Count citations
    citation_count = len(re.findall(r'\[Source \d+\]', synthesis))
    
    # Calculate coverage (how many sources cited)
    cited_sources = set(re.findall(r'\[Source (\d+)\]', synthesis))
    coverage = len(cited_sources) / len(sources) if sources else 0
    
    # Word count
    word_count = len(synthesis.split())
    
    # Sentence count
    sentence_count = len(re.split(r'[.!?]+', synthesis))
    
    return {
        'citation_count': citation_count,
        'source_coverage': coverage * 100,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'avg_sentence_length': word_count / sentence_count if sentence_count > 0 else 0
    }


def validate_url(url: str) -> bool:
    """
    Basic URL validation
    """
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None


def truncate_text(text: str, max_length: int = 200, suffix: str = "...") -> str:
    """
    Truncate text to max length with suffix
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)].rsplit(' ', 1)[0] + suffix


def extract_domain(url: str) -> str:
    """
    Extract domain from URL
    """
    match = re.search(r'https?://(?:www\.)?([^/]+)', url)
    return match.group(1) if match else url


def calculate_diversity_score(sources: List[Dict]) -> float:
    """
    Calculate diversity of sources (different domains)
    """
    if not sources:
        return 0.0
    
    domains = [extract_domain(s.get('url', '')) for s in sources]
    unique_domains = len(set(domains))
    
    return (unique_domains / len(sources)) * 100


def format_timestamp(iso_timestamp: str) -> str:
    """
    Format ISO timestamp to readable format
    """
    from datetime import datetime
    try:
        dt = datetime.fromisoformat(iso_timestamp)
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        return iso_timestamp


def generate_research_summary_stats(research: Dict) -> Dict:
    """
    Generate summary statistics for a research
    """
    sources = research.get('sources', [])
    synthesis = research.get('synthesis', '')
    
    return {
        'source_count': len(sources),
        'total_words': len(synthesis.split()),
        'reading_time': estimate_reading_time(synthesis),
        'citation_count': len(re.findall(r'\[Source \d+\]', synthesis)),
        'diversity_score': calculate_diversity_score(sources),
        'avg_source_length': sum(len(s.get('content', '')) for s in sources) / len(sources) if sources else 0
    }
