# greeting/views.py
import os
from django.http import JsonResponse
from django.views import View
from .services import GreetingService

class GreetingView(View):
    def get(self, request):
        username = os.getenv("USER", "Usuário")
        service = GreetingService()
        greeting = service.create_greeting(username)
        return JsonResponse(greeting)

class PersonalizedGreetingView(View):
    def get(self, request, name):
        service = GreetingService()
        greeting = service.create_greeting(name)
        return JsonResponse(greeting)