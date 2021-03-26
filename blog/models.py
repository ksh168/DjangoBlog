from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # auto_now=True ->will change everytime post is updated
    # auto_now_add=True ->will be set once when post is created, but can't be changed later

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #ForeignKey as author can create multiple posts
    #on_delete ->if user is deleted all their posts too

