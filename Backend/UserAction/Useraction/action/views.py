from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework import status
from .models import Purchase, Review
from django.views.decorators.csrf import csrf_exempt
import json


class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = json.get('username')
        password = json.get('password')
        email = data.get('email')
        
        if (User.objects.filter(username=username).exists() or 
            User.objects.filter(email=email).exists()):
            return JsonResponse(
                {'error': 'Username or Email already exists'}, status=400
                )
        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({'message':'User created successfully'}, status=201)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'message':'Logged in successfully'}, status=200)
        else:
            return JsonResponse(
                {'error': 'Invalid credentials'}, status=401
                )
