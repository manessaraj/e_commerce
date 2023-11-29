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


"""Product API"""


@app.put("/products")
async def create_product(product: ProductPatch) -> Product:
    """Create a new product"""
    return await repo.product_repository.create(product.model_dump())


@app.post("/products")
async def update_product(product: ProductPatch) -> Product:
    """Update an existing product"""
    return await repo.product_repository.update(product.model_dump())


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
async def create_user(user: UserPatch) -> User:
    """Create a new user"""
    return await repo.user_repository.create(user.model_dump())


@app.post("/users")
async def update_user(user: UserPatch) -> User:
    """Update an existing user"""
    return repo.user_repository.update(user.model_dump())


@app.get("/users")
async def get_users() -> list[User]:
    """Get all users"""
    return await repo.user_repository.find_all()


@app.get("/users/{user_id}")
async def get_user(user_id: str) -> User:
    """Get a single user by id"""
    return await repo.user_repository.find_one(user_id)
