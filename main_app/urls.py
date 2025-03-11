from django.urls import path
from .views import home, dashboard, sign_in_view, logout_view, signup_view, add_book, book_list, edit_book, delete_book


urlpatterns = [
    path('', home, name='home'),
    path('signin/', sign_in_view, name='signin'),
    path('signup/', signup_view, name='signup'),  # ✅ Corrected name
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('add-book/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
    path('book/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
]

