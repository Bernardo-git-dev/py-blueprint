# services/greeting_service.py

def create_greeting(name: str):
    return {
        "message": f"Hello {name} from Flask!",
        "greeting_type": "personalized"
    }