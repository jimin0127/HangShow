from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('join/', views.join, name="join"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('login/2-1/assignment', views.getAssignment2_1, name='assignment'),
    path('login/2-2/assignment', views.getAssignment2_2, name='assignment'),
    path('login/2-3/assignment', views.getAssignment2_3, name='assignment'),
    path('login/2-4/assignment', views.getAssignment2_4, name='assignment'),
    path('login/2-5/assignment', views.getAssignment2_5, name='assignment'),
    path('login/2-6/assignment', views.getAssignment2_6, name='assignment'),

    path('calendar',views.calendar, name='calendar'),

    path('listview/',views.AssignmentList.as_view(), name='listview'),

    path('calendar/2-1/', views.calendar2_1_stu, name='calendar2-1_stu'),
    path('calendar/2-2/', views.calendar2_2_stu, name='calendar2-2_stu'),
    path('calendar/2-3/', views.calendar2_3_stu, name='calendar2-3_stu'),

    path('login/2-1/', views.calendar2_1, name='calendar2-1'),
    path('login/2-2/', views.calendar2_2, name='calendar2-2'),
    path('login/2-3/', views.calendar2_3, name='calendar2-3'),
    path('login/2-4/', views.calendar2_4, name='calendar2-4'),
    path('login/2-5/', views.calendar2_5, name='calendar2-5'),
    path('login/2-6/', views.calendar2_6, name='calendar2-6'),



]




