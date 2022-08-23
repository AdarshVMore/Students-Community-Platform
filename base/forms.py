from dataclasses import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Post, Room
from django.contrib.auth.forms import UserCreationForm


class ModifiedForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UploadPost(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['id','created']