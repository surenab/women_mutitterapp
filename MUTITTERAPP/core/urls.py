from django.urls import path
from .views import home, CreateKling,MyKlingUpdate,MyKling,MyKlingDetail


urlpatterns = [
    path("", home, name="home"),
    path("my-klings", MyKling.as_view(), name="my_klings"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
    path("my-klings-details/<int:pk>", MyKlingDetail.as_view(), name="my-kling-details"),
    path("my-klings-update/<int:pk>", MyKlingUpdate.as_view(), name="my-kling-update"),
]
