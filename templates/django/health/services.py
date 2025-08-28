# health/services.py
from datetime import datetime

class HealthService:
    def get_health_status(self):
        return {
            "status": "healthy",
            "timestamp": datetime.now().isoformat()
        }