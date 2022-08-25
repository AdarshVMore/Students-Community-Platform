from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import ModifiedForm, Profile
from .forms import RoomForm, UpdateProfile

from django.contrib.auth.decorators import login_required

from .models import Room, Topic, Message, Post
import random



# Create your views here.

rooms = [
    {'id': 1},
    {'id': 2},
    {'id': 3},
]

def loginpage(request):
    page = 'login'
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

    context = {'page':page}


    return render(request , 'base/signup.html', context)

def logoutpage(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = ModifiedForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        return redirect('login')
    context = {'form':form}
    return render(request, 'base/signup.html', context)

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
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q)).order_by('-created')

    context = {'rooms': rooms,'topics':topics, 'room_count':room_count, 'room_messages':room_messages}
    return render(request, 'base/home.html', context)

def room(request, x):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        ) 

    room_count = rooms.count() 
    topics =  Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q)).order_by('-created')


    room = Room.objects.get(id=x)
    allmessages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', x=room.id)

    context = {'room': room , 'allmessages': allmessages, 'participants':participants, 'rooms': rooms,'topics':topics, 'room_count':room_count, 'room_messages':room_messages}
    return render(request, 'base/home.html', context)

def userProfile(request, x):
    user = User.objects.get(id=x)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    topics = Topic.objects.all()
    profiles = UpdateProfile.objects.all()
    updateprofile = UpdateProfile()

    if request.method == 'POST':
        updateprofile = UpdateProfile(request.POST)
        if updateprofile.is_valid():
            updateprofile.save()
            return redirect('profile')
    context = {'user':user , 'rooms':rooms, 'room_message':room_message,'topics':topics,'updateprofile':updateprofile, 'profiles':profiles}
    return render(request, 'base/profile.html', context)

@login_required(login_url='/login')
def addroom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            room.host = request.user
            room.save()
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


@login_required(login_url='/login')
def deleteMessage(request, x):
    message = Message.objects.get(id = x)

    if request.user != message.user:
        return HttpResponse("you are not logged in!!")
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')

    

    return render(request, 'base/deleteroom.html', {'obj':message})



# Creating learn secction

def learn(request):
    posts = Post.objects.all()
    data = request.POST

    if request.method == 'POST':
        image = request.FILES.get('image')
        
        thumbnail = Post.objects.create(
            description=data['description'],
            image=image,
            subject=data['subject'],
            link=data['link'],
            user=request.user
        )
        new_context = {'thumbnail':thumbnail, 'image':image}
        return render(request, 'base/home.html', new_context)

    context = {'data':data,'posts':posts}
    return render(request, 'base/home.html',context)

@login_required(login_url='/login')
def deletePost(request, x):
    post = Post.objects.get(id = x)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'base/deletePost.html', {'obj':post})



def profile(request):
    profiles = Profile()

    if request.method == 'POST':
        profile_img = request.FILES.get('ProfilePic')
        profiles = Profile(request.POST)
        if profiles.is_valid():
            updateprofile = profiles.save()
            updateprofile.username = request.user
            updateprofile.ProfilePic = profile_img
            updateprofile.save()
            return redirect('profile') 
    context = {'profiles':profiles}
    return render(request, 'base/updateprofile.html', context)

