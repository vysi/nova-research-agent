import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from duckduckgo_search import DDGS
import config
import time

class ResearchEngine:
    """Engine for gathering research from multiple sources"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search_web(self, query: str, max_results: int = None) -> List[Dict]:
        """Search the web using DuckDuckGo with error handling"""
        
        if max_results is None:
            max_results = config.MAX_SEARCH_RESULTS
        
        results = []
        
        try:
            with DDGS() as ddgs:
                search_results = ddgs.text(query, max_results=max_results)
                
                for result in search_results:
                    results.append({
                        'title': result.get('title', 'Untitled'),
                        'url': result.get('href', ''),
                        'snippet': result.get('body', 'No description available')
                    })
        
        except Exception as e:
            print(f"Search error: {str(e)}")
            # Return empty list instead of crashing
            return []
        
        return results
    
    def fetch_content(self, url: str) -> str:
        """Fetch and extract main content from a URL with better error handling"""
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
                script.decompose()
            
            # Try to find main content
            main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
            
            if main_content:
                text = main_content.get_text()
            else:
                text = soup.get_text()
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            # Limit length
            if len(text) > config.MAX_CONTENT_LENGTH:
                text = text[:config.MAX_CONTENT_LENGTH] + "..."
            
            # Validate we got meaningful content
            if len(text) < 100:
                return f"Content too short or unavailable from {url}"
            
            return text
        
        except requests.Timeout:
            return f"Timeout: Could not fetch content from {url} (took too long)"
        except requests.RequestException as e:
            return f"Request error: Could not access {url} - {str(e)}"
        except Exception as e:
            return f"Error extracting content from {url}: {str(e)}"
    
    def gather_research(self, query: str) -> List[Dict]:
        """Gather research from multiple sources"""
        
        # Search for sources
        search_results = self.search_web(query)
        
        sources = []
        
        for result in search_results:
            # Fetch full content
            content = self.fetch_content(result['url'])
            
            if content and not content.startswith("Error"):
                sources.append({
                    'title': result['title'],
                    'url': result['url'],
                    'snippet': result['snippet'],
                    'content': content
                })
            
            # Be respectful with requests
            time.sleep(0.5)
        
        return sources
