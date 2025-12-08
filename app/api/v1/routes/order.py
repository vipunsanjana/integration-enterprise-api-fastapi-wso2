from fastapi import APIRouter
from app.models.order import OrderCreate, OrderResponse
from app.services.order_service import create_order, get_orders

router = APIRouter()

@router.post("/create", response_model=OrderResponse)
def create(order: OrderCreate):
    return create_order(order)

@router.get("/all", response_model=list[OrderResponse])
def list_orders():
    return get_orders()
