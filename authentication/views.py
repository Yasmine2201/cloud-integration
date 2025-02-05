from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

from authentication.forms import RegistrationForm, LoginForm


# Create your views here.


# Create your views here.
def welcome_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'authentication/welcome.html')
def registration_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'authentication/register.html', {'form': form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'authentication/login.html', {'form': form})

def logout_user(request):

    logout(request)
    return redirect('welcome')