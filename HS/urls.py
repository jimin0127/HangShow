from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('join/', views.join, name="join"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('assignment/', views.getAssignment, name='assignment'),
    path('calendar/',views.calendar, name='calendar'),
    path('listview/',views.AssignmentList.as_view(), name='listview'),


]




