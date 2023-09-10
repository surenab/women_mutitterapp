from django.contrib import admin
from .models import Kling, Message,KlingComment,Tag

# Register your models here.
class KlingCommentAdmin(admin.ModelAdmin):
    list_display = ["owner", "text"]

    


class KlingAdmin(admin.ModelAdmin):
    list_display=("id","created_on","title","text","kling_type","kling_category","user","image")
    list_filter=("title","text","user","kling_category")
    search_fields=("kling_type","title")
    filter_horizontal=("tags",)
    
admin.site.register(Kling,KlingAdmin)    
admin.site.register(Message)
admin.site.register(KlingComment)
admin.site.register(Tag)

