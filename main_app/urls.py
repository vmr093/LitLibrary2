from django.urls import path
from .views import home, dashboard, sign_in_view, logout_view, signup_view, add_book, book_list


urlpatterns = [
    path('', home, name='home'),
    path('signin/', sign_in_view, name='signin'),
    path('signup/', signup_view, name='signup'),  # ✅ Corrected name
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('add-book/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
]

