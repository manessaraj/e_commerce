from fastapi import FastAPI
import src.repository as repo
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to E-Commerce App"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/testdb")
async def test():
    response = repo.test_db_connection()
    return {"message": response}