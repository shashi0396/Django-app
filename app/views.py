import os
from django.http import JsonResponse

def hello(request):
    version = os.getenv("APP_VERSION", "v1")
    return JsonResponse({
        "message": f"Hello from Django CI/CD 🚀 ({version})"
    })

def health(request):
    return JsonResponse({
        "status": "ok"
    })