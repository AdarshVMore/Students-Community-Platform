from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, Post, UpdateProfile


admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(UpdateProfile)
