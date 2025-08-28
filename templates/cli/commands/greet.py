# commands/greet.py
from services import greeting_service

def execute(name, verbose=False):
    """Executa o comando de saudação."""
    message = greeting_service.create_greeting(name)
    print(message["message"])
    
    if verbose:
        print(f"Tipo de saudação: {message['greeting_type']}")