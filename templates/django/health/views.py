# health/views.py
from django.http import JsonResponse
from django.views import View
from .services import HealthService
from datetime import datetime

class HealthView(View):
    def get(self, request):
        service = HealthService()
        status = service.get_health_status()
        return JsonResponse(status)