from pydantic import BaseModel

class ProductSize(BaseModel):
    size: str
    stock: int

class Product(BaseModel):
    title: str
    description: str
    price: float
    image: str
    categories: list[str]
    tags: list[str]
    sizes: list[ProductSize]

class ProductPatch(BaseModel):
    title: str | None
    description: str | None
    price: float | None
    image: str | None
    categories: list[str] | None
    tags: list[str] | None
    sizes: list[ProductSize] | None

class OrderItem(BaseModel):
    productId: str
    quantity: int

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str
    id: str
    country: str

class Order(BaseModel):
    items: list[OrderItem]
    shippingAddress: Address
    billingAddress: Address
    totalPrice: float
    orderId: str
    status: str
    paymentMethod: str
    transactionId: str


class User(BaseModel):
    email: str
    firstName: str
    lastName: str
    addresses: list[Address]
    defaultAddressId: str
    phone: str

class Cart(BaseModel):
    items: list[OrderItem]
    totalPrice: float
    userId: str

class Transaction(BaseModel):
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

