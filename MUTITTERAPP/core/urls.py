from django.urls import path

from .views import Home, CreateKling, MyKling

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
    path("my-kling", MyKling.as_view(), name="my_kling"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
