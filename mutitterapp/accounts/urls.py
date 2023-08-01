from django.urls import path, include
from .views import Register, signup_login

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', signup_login, name="signup_login"),
    path('register', Register.as_view(), name='register'),
]