import requests

BASE_URL = "http://127.0.0.1:8000"


def test_create_and_low_stock():
    product = {
        "name": "Keyboard",
        "price": 50,
        "category": "Tech",
        "stock": 3
    }

    r = requests.post(f"{BASE_URL}/products", json=product)
    assert r.status_code == 200

    r = requests.get(f"{BASE_URL}/products/low-stock?threshold=5")
    assert r.status_code == 200

    data = r.json()
    assert any(p["name"] == "Keyboard" for p in data)
