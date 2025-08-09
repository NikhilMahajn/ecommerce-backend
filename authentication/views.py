from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            User.objects.create_user(username=email,password=password)
            return Response({'user created successully'})
            
        except Exception as e:
            return Response("Error: " + str(e))
        
    return Response({'use get api'})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        try:
            email = request.data.get('email')
            password = request.data.get('password')
        
            user = authenticate(request, username=email, password=password)
            if user is None:
                return Response({'error': 'Invalid email or password'})
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        except Exception as e:
            return Response("Error: " + str(e))
  