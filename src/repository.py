from motor.motor_asyncio import AsyncIOMotorClient
import os
client = AsyncIOMotorClient(os.environ.get("MONGO_URI"))
db = client.get_database(os.environ.get("DB_NAME"))