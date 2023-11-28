from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
client = AsyncIOMotorClient(os.environ.get("MONGO_URI"))
db = client.main

def test_db_connection() -> str:
    try:
        client.admin.command('ping')
    except Exception as e:
        return f"Exception occurred: {e}"
    return "Pinged your deployment. You successfully connected to MongoDB!"