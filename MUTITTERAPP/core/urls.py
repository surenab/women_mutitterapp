from django.urls import path
from .views import home, CreateKling, MyKling


urlpatterns = [
    path("", home, name="home"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
    path("my_kling", MyKling.as_view(), name="my_kling"),
]
