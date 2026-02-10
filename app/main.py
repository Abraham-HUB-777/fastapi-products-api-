from fastapi import FastAPI
from typing import List
from app.models import Product, ProductCreate
from app.service import ProductService

app = FastAPI()
service = ProductService()


@app.post("/products", response_model=Product)
def create_product(product: ProductCreate):
    return service.create_product(product)


@app.get("/products/low-stock", response_model=List[Product])
def get_low_stock(threshold: int):
    return service.low_stock(threshold)
