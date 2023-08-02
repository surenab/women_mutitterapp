from django.urls import path, include
from .views import signup_login, home
from .views import Register, signup_login, home


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', signup_login, name="signup_login"),
    path('home/', home, name="home"),
    path('register', Register.as_view(), name='register'),
]

