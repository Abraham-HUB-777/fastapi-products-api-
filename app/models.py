from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str
    price: float = Field(gt=0)
    category: str
    stock: int = Field(ge=0)


class Product(ProductCreate):
    id: int
