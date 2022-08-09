from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('room/<str:x>', views.room, name = 'room'),
    
    path('addroom/', views.addroom , name = 'addroom'),
    path('updateroom/<str:x>/', views.updateRoom , name = 'updateroom'),
    path('deleteroom/<str:x>/', views.deleteRoom , name = 'deleteroom'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),



]