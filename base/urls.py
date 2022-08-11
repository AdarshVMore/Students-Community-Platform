from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),

    path('', views.home, name = 'home'),
    path('room/<str:x>', views.room, name = 'room'),
    path('profile/<str:x>', views.userProfile, name = 'profile'),

    path('addroom/', views.addroom , name = 'addroom'),
    path('updateroom/<str:x>/', views.updateRoom , name = 'updateroom'),
    path('deleteroom/<str:x>/', views.deleteRoom , name = 'deleteroom'),
    path('deletemessage/<str:x>/', views.deleteMessage , name = 'deletemessage'),


    




]