import os
from typing import Generic, TypeVar

from motor.motor_asyncio import AsyncIOMotorClient

from src.models.models import Product, User

client = AsyncIOMotorClient(os.environ.get("MONGO_URI"))
db = client.main


def test_db_connection() -> str:
    try:
        client.admin.command("ping")
    except Exception as e:
        return f"Exception occurred: {e}"
    return "Pinged your deployment. You successfully connected to MongoDB!"


T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, collection: str):
        self.collection = collection

    async def find_all(self) -> list[T]:
        return await db[self.collection].find().to_list(length=100)

    async def find_one(self, id: str) -> T:
        return await db[self.collection].find_one({"_id": id})

    async def create(self, data: dict) -> T:
        return await db[self.collection].insert_one(data)

    async def update(self, id: str, data: dict) -> T:
        return await db[self.collection].update_one({"_id": id}, {"$set": data})

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
