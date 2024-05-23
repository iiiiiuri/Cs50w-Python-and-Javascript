from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    # Check the type of instance
    if isinstance(instance, User):
        directory = 'user_{0}/images'.format(instance.username)
    elif isinstance(instance, Post):
        directory = 'user_{0}/images'.format(instance.owner.username)
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(directory, filename)

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to=path_and_rename, default="profile_pictures/defaultUser.png")
    background_picture = models.ImageField(upload_to=path_and_rename, default="background_pictures/defaultBackground.png")
    followers = models.ManyToManyField("self", related_name="following", symmetrical=False)

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    image = models.ImageField(upload_to=path_and_rename, blank=True, null=True)

    def is_liked_by_user(self, user):
        return self.likes.filter(id=user.id).exists()

    def __str__(self):
        return f"{self.owner}: {self.content[:50]}..."