import json
import os
from typing import List, Optional
from threading import Lock
from models.order import Order


class OrderRepository:
    def __init__(self, data_file: str = "data/orders.json"):
        self.data_file = data_file
        self.lock = Lock()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.data_file):
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def _read_data(self) -> list:
        with self.lock:
            with open(self.data_file, 'r') as f:
                return json.load(f)

    def _write_data(self, data: list):
        with self.lock:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)

    def save(self, order: Order) -> None:
        data = self._read_data()
        data.append(order.model_dump())
        self._write_data(data)

    def find_by_user_id(self, user_id: str) -> List[Order]:
        data = self._read_data()
        return [Order(**item) for item in data if item['user_id'] == user_id]

    def find_by_id(self, order_id: str) -> Optional[Order]:
        data = self._read_data()
        for item in data:
            if item['id'] == order_id:
                return Order(**item)
        return None
