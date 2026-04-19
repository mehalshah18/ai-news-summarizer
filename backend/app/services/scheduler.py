from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.news_fetcher import fetch_news, CATEGORIES
from app.services.summarizer import summarize_article
from app.database import articles_collection
from datetime import datetime

scheduler = AsyncIOScheduler()

async def fetch_and_summarize():
    print(f"[{datetime.utcnow()}] Running scheduled news fetch...")
    for category in CATEGORIES:
        articles = await fetch_news(category)
        for article in articles:
            exists = await articles_collection.find_one({"url": article["url"]})
            if exists:
                continue
            try:
                ai_data = await summarize_article(article["title"], article["content"])
                article.update(ai_data)
            except Exception as e:
                print(f"Summarization failed: {e}")
                article["summary"] = None
                article["sentiment"] = "neutral"
                article["tags"] = []
            await articles_collection.insert_one(article)
    print("Fetch complete.")

def start_scheduler():
    scheduler.add_job(fetch_and_summarize, "interval", hours=1, id="news_job")
    scheduler.start()
