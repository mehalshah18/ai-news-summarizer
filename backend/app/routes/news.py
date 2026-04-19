from fastapi import APIRouter, Query
from app.database import articles_collection

router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/")
async def get_news(
    category: str = Query(default=None),
    sentiment: str = Query(default=None),
    limit: int = Query(default=20, le=50)
):
    query = {}
    if category:
        query["category"] = category
    if sentiment:
        query["sentiment"] = sentiment

    cursor = articles_collection.find(query, {"_id": 0}).sort("published_at", -1).limit(limit)
    articles = await cursor.to_list(length=limit)
    return {"articles": articles, "count": len(articles)}

@router.post("/refresh")
async def manual_refresh():
    from app.services.scheduler import fetch_and_summarize
    import asyncio
    asyncio.create_task(fetch_and_summarize())
    return {"message": "News refresh triggered"}
