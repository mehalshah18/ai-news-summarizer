import httpx
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"
CATEGORIES = ["technology", "business", "health", "science", "sports"]

async def fetch_news(category: str = "technology", page_size: int = 10):
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={
            "category": category,
            "pageSize": page_size,
            "language": "en",
            "apiKey": NEWS_API_KEY
        })
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return [
            {
                "title": a["title"],
                "url": a["url"],
                "source": a["source"]["name"],
                "category": category,
                "published_at": a["publishedAt"],
                "content": a.get("description", "") or ""
            }
            for a in articles if a.get("title") and a.get("url")
        ]
