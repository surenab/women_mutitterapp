from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Kling(models.Model):
    KLING_TYPES = (("1", "Hot"), ("2", "Standard"), ("3", "Relaxing"))
    created_on = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kling_type = models.CharField(choices=KLING_TYPES, default="2", max_length=1)

    def __str__(self) -> str:
        return f"{self.title}"
