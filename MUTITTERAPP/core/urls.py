from django.urls import path
from .views import home, CreateKling, MyKlingDelete


urlpatterns = [
    path("", home, name="home"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
    path("delete-kling", MyKlingDelete.as_view(), name="delete_kling"),
]
