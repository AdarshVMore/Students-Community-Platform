from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import RoomForm
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Room, Topic

rooms = [
    {'id': 1, 'name':'adarsh'},
    {'id': 2, 'name':'bittu'},
    {'id': 3, 'name':'yash'},
]

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'wrong password or username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'wrong username or password')

    context = {}


    return render(request , 'base/signup.html', context)

def logoutpage(request):
    logout(request)
    return redirect('home')

def home(request):
    # Serching Algorithm 
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        ) 

    room_count = rooms.count() 
    topics =  Topic.objects.all()
    context = {'rooms': rooms,'topics':topics, 'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request, x):
    room = Room.objects.get(id=x)
    # for i in rooms:
    #     if i['id'] == int(x):
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

@login_required(login_url='/login')
def addroom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    context = {'form':form}
    return render(request, 'base/addroom.html', context)

@login_required(login_url='/login')
# edit or update a room (section)
def updateRoom(request, x):
    room = Room.objects.get(id = x)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("you are not logged in!!")

    context = {'form': form}
    return render(request, 'base/addroom.html', context)

@login_required(login_url='/login')
def deleteRoom(request, x):
    room = Room.objects.get(id = x)

    if request.user != room.host:
        return HttpResponse("you are not logged in!!")
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    

    return render(request, 'base/deleteroom.html', {'obj':room})
