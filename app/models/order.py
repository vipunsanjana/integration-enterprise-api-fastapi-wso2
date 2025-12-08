from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: int
    product: str
    amount: float

class OrderResponse(OrderCreate):
    id: int
    created_at: datetime
