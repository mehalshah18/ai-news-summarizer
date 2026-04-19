from pydantic import BaseModel
from typing import Optional, List

class Article(BaseModel):
    model_config = {"arbitrary_types_allowed": True}
    
    title: str
    url: str
    source: str
    category: str
    published_at: str
    summary: Optional[str] = None
    sentiment: Optional[str] = None
    tags: Optional[List[str]] = []
    