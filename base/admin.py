from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, Profile, Post, LikePost, FollowersCount


admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)