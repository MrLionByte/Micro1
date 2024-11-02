from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import HttpRequest, JsonResponse, HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import jwt

import logging

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
def xassert(request, path):
    logger.info("PATH : ", path)
    return HttpResponse(f"Received path: {path}")

class Gateway(View):
    def dispatch(self, request, *args: json, **kwargs: json) -> HttpResponse:
        path = kwargs.get('path', '')
        print("PATH :" ,path)
        if request.path.startswith('/user_action'):
            base_url = f"{settings.USER_SERVICE_URL}/{path}"
            return HttpResponse(f"Received path: {base_url}")
        elif request.path.startswith('/admin_action'):
            base_url = f"{settings.ADMIN_SERVICE_URL}/{path}"
        else:
            return JsonResponse({"error": "Invalid service"}, status=400)

        token = request.headers.get('Authorization','').split("Bearer")[-1].strip()
        
        if not self.verify_jwt(token):
            return JsonResponse({"error": "Invalid or expired JWT"}, status=401)
        
        method = request.method.lower()
        headers = {
            'Authorization': request.headers.get('Authorization', ''),
            'Content-Type': request.headers.get('Content-Type', 'application/json'),
        }

        try:
            if method == 'options':
                response = HttpResponse()
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
                response["Access-Control-Allow-Headers"] = "Authorization, Content-Type, X-CSRFToken"
                response["Access-Control-Allow-Credentials"] = "true"
                return response
            data = json.loads(request.body) if request.body else {}
                
                # Forward the request to the appropriate service
            response = requests.request(
                    method,
                    base_url,
                    json=data,
                    headers=headers,
                    params=request.GET
                )

            # Build response from the service's response
            django_response = HttpResponse(
                content=response.content,
                status=response.status_code,
                content_type=response.headers.get('Content-Type')
            )

            # Add CORS headers
            django_response["Access-Control-Allow-Origin"] = "*"
            django_response["Access-Control-Allow-Credentials"] = "true"

            return django_response
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    
    def verify_jwt(self, token: str) -> bool:
        if token == settings.DEVELOPMENT_TOKEN:
            return True
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False