import json
import os
from typing import List, Optional
from threading import Lock
from models.product import Product


class ProductRepository:
    def __init__(self, data_file: str = "data/products.json"):
        self.data_file = data_file
        self.lock = Lock()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.data_file):
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def _read_data(self) -> List[dict]:
        with self.lock:
            with open(self.data_file, 'r') as f:
                return json.load(f)

    def _write_data(self, data: List[dict]):
        with self.lock:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)

    def find_all(self) -> List[Product]:
        data = self._read_data()
        return [Product(**item) for item in data]

    def find_by_id(self, product_id: str) -> Optional[Product]:
        data = self._read_data()
        for item in data:
            if item['id'] == product_id:
                return Product(**item)
        return None

    def update(self, product: Product) -> None:
        data = self._read_data()
        for i, item in enumerate(data):
            if item['id'] == product.id:
                data[i] = product.model_dump()
                self._write_data(data)
                return
        raise ValueError(f"Product with id {product.id} not found")

    def save(self, product: Product) -> None:
        data = self._read_data()
        data.append(product.model_dump())
        self._write_data(data)
