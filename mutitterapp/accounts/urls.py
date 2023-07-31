from django.urls import path, include
from .views import signup_login

urlpatterns = [
    path('', signup_login, name="signup_login"),
]