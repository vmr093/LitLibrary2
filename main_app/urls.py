from django.urls import path
from .views import home, dashboard, sign_in_view, sign_up_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('signin/', sign_in_view, name='signin'),
    path('signup/', sign_up_view, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
