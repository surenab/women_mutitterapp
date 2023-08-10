from django.urls import path
from .views import home, CreateKling,MyKlingUpdate


urlpatterns = [
    path("", home, name="home"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
    path("my-klings/update/<int:pk>", MyKlingUpdate.as_view(), name="my_kling_update"),
]
