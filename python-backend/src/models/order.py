from pydantic import BaseModel, Field
from typing import List


class OrderItem(BaseModel):
    product_id: str
    product_name: str
    quantity: int = Field(gt=0, description="Quantity must be positive")
    price_at_purchase: float = Field(gt=0, description="Price must be positive")

    class Config:
        json_schema_extra = {
            "example": {
                "product_id": "prod-001",
                "product_name": "Wireless Headphones",
                "quantity": 2,
                "price_at_purchase": 149.99
            }
        }


class Order(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
    total: float = Field(gt=0, description="Total must be positive")
    created_at: str
    status: str = "completed"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "order-001",
                "user_id": "user1",
                "items": [
                    {
                        "product_id": "prod-001",
                        "product_name": "Wireless Headphones",
                        "quantity": 2,
                        "price_at_purchase": 149.99
                    }
                ],
                "total": 299.98,
                "created_at": "2024-01-01T12:00:00Z",
                "status": "completed"
            }
        }
