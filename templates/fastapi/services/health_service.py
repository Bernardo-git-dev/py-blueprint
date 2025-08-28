# services/health_service.py
from datetime import datetime

def get_health_status():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }