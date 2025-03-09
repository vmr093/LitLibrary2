from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm

def home(request):
    return render(request, 'main/home.html')

def sign_in_view(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect after login

    return render(request, 'main/signin.html', {'form': form})

def sign_up_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect after signup

    return render(request, 'main/signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout
