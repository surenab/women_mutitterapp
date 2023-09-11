from django.urls import path
from .views import Home, CreateKling,MyKlingUpdate,MyKlingDelete,MessageView, about, KlingDetailview, KlingCommentView, CreateKlingComment, edit_profile, view_profile, subscribe
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("create-kling", CreateKling.as_view(), name="create_kling"),
    path("my-klings-update/<int:pk>", MyKlingUpdate.as_view(), name="my-kling-update"),
    path("my-klings/delete/<int:pk>", MyKlingDelete.as_view(), name="my_kling_delete"),
    path("about", about, name="about"),
    path("kling/<int:pk>/", KlingDetailview.as_view(), name="post"),
    path('kling/<int:pk>/comment/', KlingCommentView.as_view(), name='kling-comment'),
    path("create-comment", CreateKlingComment.as_view(), name="create_comment"),
    path("contact",  MessageView.as_view(), name="contact"),
    path('profile/', view_profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('', subscribe, name='subscribe')
    
    
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
