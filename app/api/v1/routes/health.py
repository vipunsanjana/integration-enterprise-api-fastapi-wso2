from fastapi import APIRouter

router = APIRouter()

@router.get("/check")
def health_check():
    return {
        "service": "FastAPI Backend",
        "status": "UP"
    }
