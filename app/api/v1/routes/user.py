from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_users

router = APIRouter()

@router.post("/create", response_model=UserResponse)
def create(user: UserCreate):
    return create_user(user)

@router.get("/all", response_model=list[UserResponse])
def list_users():
    return get_users()
