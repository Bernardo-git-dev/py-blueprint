# PROJECT_NAME/views.py
import os
from django.http import JsonResponse

def home(request):
    username = os.getenv("USER", "Developer")
    return JsonResponse({
        "message": f"Hello {username} from Django!",
        "status": "success"
    })