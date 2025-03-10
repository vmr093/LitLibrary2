from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, SignInForm, ProfileUpdateForm
from .forms import AddBookForm
from .models import Book



def home(request):
    return render(request, 'main/home.html')

def sign_in_view(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')  # Redirect after successful login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'main/signin.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user automatically
            return redirect('dashboard')  # Redirect to dashboard.html
        else:
            print("Signup form errors:", form.errors)  # Debugging
    else:
        form = SignUpForm()

    return render(request, 'main/signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')  # Ensure this template exists

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')

    form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'main/profile.html', {'form': form})

@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)  # Show only the user's books
    return render(request, 'main/book_list.html', {'books': books})

@login_required
def add_book(request):
    form = AddBookForm()

    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')  # Redirect after adding

    return render(request, 'main/add_book.html', {'form': form})
