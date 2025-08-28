# routes/health.py
from fastapi import APIRouter
from services import health_service

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")
async def health_check():
    return health_service.get_health_status()