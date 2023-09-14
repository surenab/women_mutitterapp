from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Count

User = get_user_model()

class Kling(models.Model):
    KLING_TYPES = (("1", "Hot"), ("2", "Standart"), ("3", "Relaxing"))
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
    kling_type = models.CharField(choices=KLING_TYPES, max_length=1)
    kling_category = models.CharField(choices=KLING_CATEGORY, max_length=22)
    image = models.ImageField(upload_to="media/", default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} , {self.title}, {self.text}, {self.kling_category}, {self.created_on}"
    
    def comment_count(self):
        comment_count = KlingComment.objects.filter(kling=self).aggregate(
            total_comments=Count('id'),
            total_replies=Count('replies')
        )
        total_count = comment_count['total_comments'] + comment_count['total_replies']

        return total_count

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        comment_count = self.comment_count()

        if comment_count > 10:
            new_kling_type = "1"
        elif 5 <= comment_count <= 10:
            new_kling_type = "2"
        else:
            new_kling_type = "3"

        if self.kling_type != new_kling_type:
            self.kling_type = new_kling_type
            self.save(update_fields=["kling_type"])
    
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
    
class CommentReply(models.Model):
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
    
class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    subscribed_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email