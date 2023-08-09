from django.urls import path
from .views import home, CreateKling


urlpatterns = [
    path("", home, name="home"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
]
