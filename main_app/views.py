from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'books/index.html', {'books': books})