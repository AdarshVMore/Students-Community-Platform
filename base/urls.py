from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),

    path('', views.home, name = 'home'),
    path('room/<str:x>', views.room, name = 'room'),
    path('profile/<str:x>', views.userProfile, name = 'profile'),
    path('updateprofile/', views.profile, name='updateprofile'),

    path('addroom/', views.addroom , name = 'addroom'),
    path('updateroom/<str:x>/', views.updateRoom , name = 'updateroom'),
    path('deleteroom/<str:x>/', views.deleteRoom , name = 'deleteroom'),
    path('deletemessage/<str:x>/', views.deleteMessage , name = 'deletemessage'),

    path('learn/', views.learn, name='learn'),
    path('learn/viewpost/<str:x>' , views.viewpost , name='viewpost',)


    




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)