from dataclasses import fields
from secrets import choice
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Post, Room, UpdateProfile
from django.contrib.auth.forms import UserCreationForm


class ModifiedForm(UserCreationForm):
    email = forms.EmailField()
    Year = forms.CharField(max_length=100)
    Branch = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'Year', 'Branch']

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

class Profile(ModelForm):
    class Meta:
        model = UpdateProfile
        fields = '__all__'
