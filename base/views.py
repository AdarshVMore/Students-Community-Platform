from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Room

rooms = [
    {'id': 1, 'name':'adarsh'},
    {'id': 2, 'name':'bittu'},
    {'id': 3, 'name':'yash'},
]

def home(request, ):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, x):
    room = Room.objects.get(id=x)
    # for i in rooms:
    #     if i['id'] == int(x):
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)