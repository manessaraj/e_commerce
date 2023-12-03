import os
from typing import Generic, TypeVar

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from src.models.models import Product, User

client = AsyncIOMotorClient(os.environ.get("MONGO_URI"))
# print(f'Connecting to {os.environ.get("MONGO_URI")}: {os.environ.get("DB_NAME")}')
db = client[os.environ.get("DB_NAME")]


def test_db_connection() -> str:
    try:
        client.admin.command("ping")
    except Exception as e:
        return f"Exception occurred: {e}"
    return "Pinged your deployment. You successfully connected to MongoDB!"


T = TypeVar("T")


class BaseRepository(Generic[T]):
    @staticmethod
    async def clean_db(collection_name: str = None) -> str:
        if collection_name:
            await db[collection_name].drop()
            return f"Collection {collection_name} dropped!"
        return "Nothing dropped!"

    def __init__(self, collection: str):
        self.collection = collection

    async def find_all(self) -> list[T]:
        return await db[self.collection].find().to_list(length=100)

    async def find_one(self, id: str) -> T:
        obj = await db[self.collection].find_one({"_id": ObjectId(id)})
        return obj

    async def create(self, data: dict) -> T:
        result = await db[self.collection].insert_one(data)
        return await self.find_one(result.inserted_id)

    def _merge_patch(self, obj: dict, data: dict) -> dict:
        for key, value in data.items():
            if value is not None:
                obj[key] = value
        return obj

    async def update(self, id: str, data: dict) -> T:
        obj = await self.find_one(id)
        data = self._merge_patch(obj, data)
        _ = await db[self.collection].update_one({"_id": ObjectId(id)}, {"$set": data})
        return await self.find_one(id)

    async def delete(self, id: str) -> None:
        return await db[self.collection].delete_one({"_id": id})


class ProductRepository(BaseRepository[Product]):
    def __init__(self):
        super().__init__("products")


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__("users")


product_repository = ProductRepository()
user_repository = UserRepository()
