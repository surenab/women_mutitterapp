from django.contrib import admin
from .models import Kling, Message,KlingComment

# Register your models here.
class KlingCommentAdmin(admin.ModelAdmin):
    list_display = ["owner", "text"]

    
admin.site.register(Kling)
admin.site.register(Message)
admin.site.register(KlingComment)

