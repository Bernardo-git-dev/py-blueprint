# controllers/greeting_controller.py
from services import greeting_service

def handle_greeting(name: str):
    return greeting_service.create_greeting(name)