from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    name: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "id": "user1",
                "name": "Alice Johnson",
                "email": "alice.johnson@example.com"
            }
        }
