import json
import os
from typing import Optional
from threading import Lock
from models.cart import Cart


class CartRepository:
    def __init__(self, data_file: str = "data/carts.json"):
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

    def find_by_user_id(self, user_id: str) -> Optional[Cart]:
        data = self._read_data()
        for item in data:
            if item['user_id'] == user_id:
                return Cart(**item)
        return None

    def save(self, cart: Cart) -> None:
        data = self._read_data()
        # Update existing cart or add new one
        found = False
        for i, item in enumerate(data):
            if item['user_id'] == cart.user_id:
                data[i] = cart.model_dump()
                found = True
                break
        if not found:
            data.append(cart.model_dump())
        self._write_data(data)

    def delete(self, user_id: str) -> None:
        data = self._read_data()
        data = [item for item in data if item['user_id'] != user_id]
        self._write_data(data)
