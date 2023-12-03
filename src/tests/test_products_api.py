from fastapi.testclient import TestClient

from src.main import app
from src.models.models import Product
from src.tests.test_utils import create_random_object

client = TestClient(app)


class TestProducts:
    def test_get_products(self):
        response = client.get("/products")
        assert response.status_code == 200
        assert response.json() == []

    def _create_product(self):
        mocked_product = create_random_object(Product)
        response = client.put("/products", json=mocked_product.model_dump())
        return mocked_product, response

    def test_create_product(self):
        mocked_product, response = self._create_product()
        assert response.status_code == 200
        assert response.json()["title"] == mocked_product.title
        assert response.json()["description"] == mocked_product.description
        assert self.response.json()["_id"] is not None, "Id can't be null"

    def test_read_product(self):
        _, response = self._create_product()
        product = Product(**response.json())
        response = client.get(f"/products/{product._id}")
        assert response.status_code == 200
        assert response.json()["_id"] == product._id
