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
    
    def comment_count(self):
        return self.klingcomment_set.count()
    
    class Meta:
        ordering = ['-created_on']

class Message(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=700)
    
class KlingComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    kling = models.ForeignKey(Kling, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.owner.username} commented {self.text}"
    
class KlingReply(models.Model):
    comment = models.ForeignKey(KlingComment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username
