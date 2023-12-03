import os

from fastapi import FastAPI

import src.repository as repo
from src.models.models import Product, ProductPatch, User, UserPatch

app = FastAPI()


@app.get("/")
async def root():
    """Root test endpoint"""
    return {"message": "Welcome to E-Commerce App"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Test endpoint with path parameter"""
    return {"item_id": item_id}


@app.get("/testdb")
async def test():
    """Endpoint to check connection to MongoDB"""
    response = repo.test_db_connection()
    return {"message": response}


@app.get("/cleandb/{collection_name}")
async def clean_db(collection_name: str = None):
    """Endpoint to clean MongoDB"""
    response = await repo.BaseRepository.clean_db(collection_name=collection_name)
    return {"message": response}


"""Product API"""


@app.put("/products")
async def create_product(product: Product) -> Product:
    """Create a new product"""
    obj = await repo.product_repository.create(data=product.model_dump())
    return obj


@app.post("/products/{product_id}")
async def update_product(product_id: str, product: ProductPatch) -> Product:
    """Update an existing product"""
    return await repo.product_repository.update(
        id=product_id, data=product.model_dump()
    )


@app.get("/products")
async def get_products() -> list[Product]:
    """Get all products"""
    return await repo.product_repository.find_all()


@app.get("/products/{product_id}")
async def get_product(product_id: str) -> Product:
    """Get a single product"""
    return await repo.product_repository.find_one(product_id)


""" User API """


@app.put("/users")
async def create_user(user: User) -> User:
    """Create a new user"""
    return await repo.user_repository.create(user.model_dump())


@app.post("/users/{user_id}")
async def update_user(user_id: str, user: UserPatch) -> User:
    """Update an existing user"""
    return repo.user_repository.update(id=user_id, data=user.model_dump())


@app.get("/users")
async def get_users() -> list[User]:
    """Get all users"""
    return await repo.user_repository.find_all()


@app.get("/users/{user_id}")
async def get_user(user_id: str) -> User:
    """Get a single user by id"""
    return await repo.user_repository.find_one(user_id)


if __name__ == "__main__" and os.environ.get("DEBUG_MODE") != "false":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
