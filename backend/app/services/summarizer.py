import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

async def summarize_article(title: str, content: str) -> dict:
    prompt = f"""
You are a professional news analyst. Given the article title and content below,
return a JSON object with exactly these three keys:
- "summary": a 2-3 sentence plain-English summary
- "sentiment": one of "positive", "neutral", or "negative"
- "tags": a list of 3-5 relevant topic tags (lowercase, no hashtags)

Article Title: {title}
Article Content: {content}

Respond ONLY with valid JSON. No markdown, no explanation.
"""
    response = model.generate_content(prompt)
    text = response.text.strip()
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)

