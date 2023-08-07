from django.urls import path, include
from .views import home, CreateCackling


urlpatterns = [
    path("", home, name="home"),
    path("create-cackling", CreateCackling.as_view(), name="create_cackling"),
]
