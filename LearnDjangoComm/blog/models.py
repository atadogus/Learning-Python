from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from dataclasses import dataclass


@dataclass
class Post(models.Model):
    """A class to make the storage of posts in the website easier"""

    title: str = models.CharField(max_length=100)
    content: str = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author: str = models.ForeignKey(User, on_delete=models.CASCADE)
