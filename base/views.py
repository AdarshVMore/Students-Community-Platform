from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import ModifiedForm
from .forms import RoomForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Room, Topic, Message, Profile, Post, LikePost, FollowersCount
from itertools import chain
import random



# Create your views here.

rooms = [
    {'id': 1, 'name':'adarsh'},
    {'id': 2, 'name':'bittu'},
    {'id': 3, 'name':'yash'},
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
    context = {'user':user , 'rooms':rooms, 
                'room_message':room_message,'topics':topics}
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









def learnSection(request):
    # user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))


    return render(request, 'base/home.html', { 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})#user_profile': user_profile

# @login_required(login_url='signin')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/learn')
    else:
        return redirect('/learn')

