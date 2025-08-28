# commands/health.py
from services import health_service

def execute(verbose=False):
    """Executa o comando de verificação de saúde."""
    status = health_service.get_health_status()
    print(f"Status: {status['status']}")
    
    if verbose:
        print(f"Timestamp: {status['timestamp']}")