from typing import Any, Optional, Type, get_type_hints

from bson import ObjectId
from pydantic import BaseModel, Field, create_model


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, *args: Any):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls):
        return {"type": "string"}


class Model(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ProductSize(BaseModel):
    size: str
    stock: int


class Product(Model):
    title: str
    description: str
    price: float
    image: str | None
    categories: list[str] | None
    tags: list[str] | None
    sizes: list[ProductSize] | None


class OrderItem(Model):
    productId: str
    quantity: int


class Address(Model):
    street: str
    city: str
    state: str
    zip: str
    id: str
    country: str


class Order(Model):
    items: list[OrderItem]
    shippingAddress: Address
    billingAddress: Address
    totalPrice: float
    orderId: str
    status: str
    paymentMethod: str
    transactionId: str


class User(Model):
    email: str
    firstName: str
    lastName: str
    addresses: list[Address]
    defaultAddressId: str
    phone: str


class Cart(Model):
    items: list[OrderItem]
    totalPrice: float
    userId: str


class Transaction(Model):
    orderId: str
    paymentMethod: str
    transactionId: str
    status: str
    amount: float
    currency: str
    createdAt: str
    updatedAt: str
    userId: str
    shippingAddress: Address
    billingAddress: Address


def create_patch_model(model: Type[BaseModel]) -> Type[BaseModel]:
    """
    Create a new Pydantic model where all attributes of the given model are optional.
    """
    fields = {
        field_name: (Optional[field_type], None)
        for field_name, field_type in get_type_hints(model).items()
    }

    patch_model = create_model(f"{model.__name__}Patch", **fields)
    return patch_model


TransactionPatch = create_patch_model(Transaction)
UserPatch = create_patch_model(User)
AddressPatch = create_patch_model(Address)
ProductPatch = create_patch_model(Product)
