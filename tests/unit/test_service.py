from app.service import ProductService
from app.models import ProductCreate


def test_low_stock_returns_products_below_threshold():
    service = ProductService()

    service.create_product(ProductCreate(
        name="Laptop",
        price=1000,
        category="Tech",
        stock=10
    ))

    service.create_product(ProductCreate(
        name="Mouse",
        price=25,
        category="Tech",
        stock=2
    ))

    result = service.low_stock(5)

    assert len(result) == 1
    assert result[0].name == "Mouse"
