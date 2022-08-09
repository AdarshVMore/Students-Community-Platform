from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
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
    # participants = 
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
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]