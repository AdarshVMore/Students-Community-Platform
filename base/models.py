from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# one topic can have many Rooms , one room can have many users , one user can have many messages
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # null means empyt description which by default is false meaning it cant be kept empty by setting it to true u say you can keep description box blank
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name



# one to many relationship , one user can have many messages
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.body[0:50]







# social media app

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    subject = models.CharField(max_length=200)
    link = models.URLField(blank=True) 
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
