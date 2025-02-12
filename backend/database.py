from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)

db = client.ollama_kurbanayt