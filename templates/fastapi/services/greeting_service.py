# services/greeting_service.py

def create_greeting(name: str):
    return {
        "message": f"Hello {name} from FastAPI!",
        "greeting_type": "personalized"
    }