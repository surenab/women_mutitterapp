from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Kling(models.Model):
    KLING_TYPES = (("1", "Hot"), ("2", "Standard"), ("3", "Relaxing"))
    KLING_CATEGORY = (
        ("Life and Love", "Life and Love"),
        ("Travel and Adventure", "Travel and Adventure"),
        ("Art and Music", "Art and Music"),
        ("Nature", "Nature"),
        ("Food and Wellness", "Food and Wellness"),
        ("Careers", "Careers"),
        ("Science and Technology", "Science and Technology"),
        ("Other", "Other"),
    )
    created_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kling_type = models.CharField(choices=KLING_TYPES, default="2", max_length=1)
    kling_category = models.CharField(choices=KLING_CATEGORY, max_length=22)
    image = models.ImageField(upload_to="media/", default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} , {self.title}, {self.kling_category}, {self.created_on}"




