from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float = Field(gt=0, description="Price must be positive")
    category: str
    inventory: int = Field(ge=0, description="Inventory must be non-negative")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "prod-001",
                "name": "Wireless Headphones",
                "description": "Premium noise-cancelling headphones",
                "price": 149.99,
                "category": "Electronics",
                "inventory": 45
            }
        }
