from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),  # Serves landing.html as the homepage
    path('about/', views.about, name='about'),  # Serves about.html
    path('books/', views.books_index, name='book-index'),  # Books index page
]
