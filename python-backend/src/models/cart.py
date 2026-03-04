from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class CartItem(BaseModel):
    product_id: str
    quantity: int = Field(gt=0, description="Quantity must be positive")
    price_at_add: float = Field(gt=0, description="Price must be positive")

    class Config:
        json_schema_extra = {
            "example": {
                "product_id": "prod-001",
                "quantity": 2,
                "price_at_add": 149.99
            }
        }


class Cart(BaseModel):
    user_id: str
    items: List[CartItem] = Field(default_factory=list)
    created_at: str
    updated_at: str

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user1",
                "items": [
                    {
                        "product_id": "prod-001",
                        "quantity": 2,
                        "price_at_add": 149.99
                    }
                ],
                "created_at": "2024-01-01T12:00:00Z",
                "updated_at": "2024-01-01T12:30:00Z"
            }
        }
