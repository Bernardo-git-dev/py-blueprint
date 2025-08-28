# services/greeting_service.py

def create_greeting(name):
    """Cria uma saudação personalizada."""
    return {
        "message": f"Olá, {name}! Saudações da sua nova CLI!",
        "greeting_type": "personalized"
    }