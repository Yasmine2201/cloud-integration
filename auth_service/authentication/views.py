from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import UserSerializer

from core_models.models import User


class RegisterView(APIView):

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username'] if 'username' in serializer.validated_data else email
            password = serializer.validated_data['password']

            if User.objects.filter(email=email).exists():
                return Response({f'error': f'This email {email} already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(username=username).exists():
                return Response({f'error': f'This username {username} already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save(password=make_password(password), username=username)
            return Response({
                'id': user.id,
                'email': user.email,
                'username': user.username,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(username=email, password=password)
            if user:
                refresh = RefreshToken.for_user(user)

                user_response = User.objects.get(email=email)
                return Response({
                    'user': {
                        'username': user_response.username,
                    },
                    'token':{
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }
                }, status=status.HTTP_200_OK)
            else :
                return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

