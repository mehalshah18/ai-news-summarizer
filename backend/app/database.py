from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import certifi
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

MONGODB_URI = os.getenv("MONGODB_URI")
print(f"DEBUG - MongoDB URI: {MONGODB_URI}")

client = AsyncIOMotorClient(
    MONGODB_URI,
    tlsCAFile=certifi.where()
)
db = client["newsdb"]
articles_collection = db["articles"]
