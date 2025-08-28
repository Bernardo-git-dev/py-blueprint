# routes/greeting.py
from fastapi import APIRouter
from controllers import greeting_controller
import os

router = APIRouter(prefix="/greeting", tags=["greeting"])

@router.get("/")
async def get_greeting():
    username = os.getenv("USER", "Usuário")
    return greeting_controller.handle_greeting(username)

@router.get("/{name}")
async def get_personalized_greeting(name: str):
    return greeting_controller.handle_greeting(name)