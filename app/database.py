from motor.motor_asyncio import AsyncIOMotorClient
import certifi
import os


MONGODB_URI = os.getenv(
    "MONGODB_URI",
    "mongodb://localhost:27017/"
)


client = AsyncIOMotorClient(MONGODB_URI)
db = client.get_database("assessment_db") 

def get_collection(name: str):
    """Return a collection object"""
    return db[name]


async def test_connection():
    try:
        await client.admin.command("ping")
        print("✅ MongoDB connection successful!")
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
