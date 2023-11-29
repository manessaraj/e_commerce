from typing import Optional, Type, get_type_hints

from pydantic import BaseModel, create_model


class IdMixin:
    _id: str


class ProductSize(BaseModel, IdMixin):
    size: str
    stock: int


class Product(BaseModel, IdMixin):
    title: str
    description: str
    price: float
    image: str
    categories: list[str]
    tags: list[str]
    sizes: list[ProductSize]


class ProductPatchV1(BaseModel, IdMixin):
    title: str | None
    description: str | None
    price: float | None
    image: str | None
    categories: list[str] | None
    tags: list[str] | None
    sizes: list[ProductSize] | None


class OrderItem(BaseModel, IdMixin):
    productId: str
    quantity: int


class Address(BaseModel, IdMixin):
    street: str
    city: str
    state: str
    zip: str
    id: str
    country: str


class Order(BaseModel, IdMixin):
    items: list[OrderItem]
    shippingAddress: Address
    billingAddress: Address
    totalPrice: float
    orderId: str
    status: str
    paymentMethod: str
    transactionId: str


class User(BaseModel, IdMixin):
    email: str
    firstName: str
    lastName: str
    addresses: list[Address]
    defaultAddressId: str
    phone: str


class Cart(BaseModel, IdMixin):
    items: list[OrderItem]
    totalPrice: float
    userId: str


class Transaction(BaseModel, IdMixin):
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
