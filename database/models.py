from datetime import datetime
from typing import List, Dict, Any

class SearchQuery:
    def __init__(self, query: str, results: List[Dict[str, Any]]):
        self.query = query
        self.results = results
        self.timestamp = datetime.utcnow()

    def to_dict(self) -> Dict:
        return {
            'query': self.query,
            'results': self.results,
            'timestamp': self.timestamp
        }

class GeneratedPage:
    def __init__(self, url: str, content: str):
        self.url = url
        self.content = content
        self.generated_at = datetime.utcnow()

    def to_dict(self) -> Dict:
        return {
            'url': self.url,
            'content': self.content,
            'generated_at': self.generated_at
        }
