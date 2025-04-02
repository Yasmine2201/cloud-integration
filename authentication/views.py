import json
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect

from authentication.models import CustomUser
from publication.services import PublicationService


# Create your views here.
def welcome_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    publications = PublicationService.get_all_publications()
    return render(request, 'welcome.html', {"all_publications": publications})

def registration_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        errors = {}
        if CustomUser.objects.filter(username=username).exists():
            errors['username'] = "Username already taken."
        if CustomUser.objects.filter(email=email).exists():
            errors['email'] = "Email already registered."

        if errors:
            return JsonResponse({"message": "Invalid data", "errors": errors}, status=400)

        # Create user manually
        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # Hash password for security
        )
        user.save()
        return JsonResponse({"message": "User created successfully", "redirection":"/login"}, status=201)
    else:
        return render(request, 'authentication/register.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": "User authenticated successfully"}, status=200)
        else:
            return JsonResponse({"errors": "Invalid credentials"}, status=400)

    return render(request, 'authentication/login.html')

def logout_user(request):

    logout(request)
    return redirect('welcome')