# services/health_service.py
from datetime import datetime

def get_health_status():
    """Obtém o status de saúde do sistema."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }