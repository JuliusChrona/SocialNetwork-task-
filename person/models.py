from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author.username}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
