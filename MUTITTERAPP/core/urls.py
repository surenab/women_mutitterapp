from django.urls import path
from .views import Home, CreateKling,MyKlingUpdate,MyKling,MyKlingDelete,MessageView, about, KlingDetailview, KlingCommentView, CreateKlingComment
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("my-klings", MyKling.as_view(), name="my_klings"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
    path("my-klings-update/<int:pk>", MyKlingUpdate.as_view(), name="my-kling-update"),
    path("my-klings/delete/<int:pk>", MyKlingDelete.as_view(), name="my_kling_delete"),
    path("about", about, name="about"),
    path("kling/<int:pk>/", KlingDetailview.as_view(), name="post"),
    path('kling/<int:pk>/comment/', KlingCommentView.as_view(), name='kling-comment'),
    path("create-comment", CreateKlingComment.as_view(), name="create_comment"),
    path("contact",  MessageView.as_view(), name="contact"),
    
    
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
