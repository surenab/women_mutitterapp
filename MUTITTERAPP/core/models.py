from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class Cackling(models.Model):
    CACKLING_TYPES = (("1", "Hot"), ("2", "Standard"), ("3", "Relaxing"))
    submit_date = models.DateTimeField()
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cackling_type = models.CharField(choices=CACKLING_TYPES, default="2", max_length=1)

    def __str__(self) -> str:
        return f"{self.title}"
