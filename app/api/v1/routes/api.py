from fastapi import APIRouter
from app.api.v1.routes.user import router as user_router
from app.api.v1.routes.order import router as order_router
from app.api.v1.routes.health import router as health_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/users", tags=["Users"])
api_router.include_router(order_router, prefix="/orders", tags=["Orders"])
api_router.include_router(health_router, prefix="/health", tags=["Health"])
