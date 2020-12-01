from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('join/', views.join, name="join"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('assignment/', views.getAssignment, name='assignment'),
    path('calendar/2-1/assignment', views.getAssignment2_1, name='assignment'),
    path('calendar/',views.calendar, name='calendar'),
    path('calendar/2-1/', views.calendar2_1, name='calendar2-1'),
    path('calendar/2-2/', views.calendar2_2, name='calendar2-2'),
    path('calendar/2-3/', views.calendar2_3, name='calendar2-3'),
    path('listview/',views.AssignmentList.as_view(), name='listview'),

]




