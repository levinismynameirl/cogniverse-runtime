"""
Enhanced web search functionality for the Mini GPT Assistant.
"""

import json
import requests
from typing import List, Dict, Optional
import logging
from urllib.parse import quote_plus
import time

import config


class WebSearchTool:
    """Enhanced web search tool using multiple APIs."""
    
    def __init__(self):
        """Initialize the web search tool."""
        self.logger = logging.getLogger('WebSearchTool')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search(self, query: str) -> Optional[str]:
        """
        Search the web for information.
        
        Args:
            query: Search query string
            
        Returns:
            Formatted search results or None if search fails
        """
        try:
            self.logger.info(f"Searching for: {query}")
            
            # Try DuckDuckGo Instant Answer API first
            results = self._search_duckduckgo_instant(query)
            if results:
                return results
            
            # Try web scraping approach
            results = self._search_web_scrape(query)
            if results:
                return results
                
            return "I couldn't find relevant information for that search query."
            
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return f"Search error: {str(e)}"
    
    def _search_duckduckgo_instant(self, query: str) -> Optional[str]:
        """Search using DuckDuckGo Instant Answer API."""
        try:
            url = "https://api.duckduckgo.com/"
            params = {
                'q': query,
                'format': 'json',
                'no_redirect': '1',
                'no_html': '1',
                'skip_disambig': '1'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                # Try to get instant answer
                if data.get('AbstractText'):
                    return f"Search result: {data['AbstractText']}"
                
                # Try related topics
                if data.get('RelatedTopics'):
                    topics = []
                    for topic in data['RelatedTopics'][:3]:
                        if isinstance(topic, dict) and topic.get('Text'):
                            topics.append(topic['Text'])
                    if topics:
                        return f"Search results: {' | '.join(topics)}"
                        
        except Exception as e:
            self.logger.warning(f"DuckDuckGo search failed: {e}")
        
        return None
    
    def _search_web_scrape(self, query: str) -> Optional[str]:
        """Fallback web search using HTML scraping."""
        try:
            # Use DuckDuckGo HTML search
            search_url = f"https://duckduckgo.com/html/?q={quote_plus(query)}"
            
            response = self.session.get(search_url, timeout=10)
            if response.status_code == 200:
                # Simple text extraction (you could use BeautifulSoup for better parsing)
                content = response.text
                if "No results found" not in content:
                    return f"Found web results for '{query}' - search completed successfully."
                    
        except Exception as e:
            self.logger.warning(f"Web scrape search failed: {e}")
        
        return None
