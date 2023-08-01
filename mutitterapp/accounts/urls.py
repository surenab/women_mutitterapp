from django.urls import path, include
from .views import signup_login, home

urlpatterns = [
    path('', signup_login, name="signup_login"),
    path('', home, name="home")
    

]