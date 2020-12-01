from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('join/', views.join, name="join"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    #path('assignment/', views.getAssignment, name='assignment'),
    # path('calendar/2-1/assignment', views.getAssignment2_1, name='assignment'),
    # path('calendar/2-2/assignment', views.getAssignment2_2, name='assignment'),
    # path('calendar/2-3/assignment', views.getAssignment2_3, name='assignment'),
    # path('calendar/',views.calendar, name='calendar'),
    # path('calendar/2-1/', views.calendar2_1, name='calendar2-1'),
    # path('calendar/2-2/', views.calendar2_2, name='calendar2-2'),
    # path('calendar/2-3/', views.calendar2_3, name='calendar2-3'),
    # path('calendar/2-4/', views.calendar2_4, name='calendar2-4'),
    # path('calendar/2-5/', views.calendar2_5, name='calendar2-5'),
    # path('calendar/2-6/', views.calendar2_6, name='calendar2-6'),

    #살리기
    path('listview/2-1/', views.AssignmentList2_1, name='listview2-1'),
    path('listview/2-2/', views.AssignmentList2_2, name='listview2-2'),
    path('listview/2-3/', views.AssignmentList2_3, name='listview2-3'),
    path('listview/2-4/', views.AssignmentList2_4, name='listview2-4'),
    path('listview/2-5/', views.AssignmentList2_5, name='listview2-5'),
    path('listview/2-6/', views.AssignmentList2_6, name='listview2-6'),
    path('listview/2-1/detail', views.detail, name = 'detail'),
    path('listview/2-2/detail', views.detail, name = 'detail'),
    path('listview/2-3/detail', views.detail, name = 'detail'),
    path('listview/2-4/detail', views.detail, name = 'detail'),
    path('listview/2-5/detail', views.detail, name = 'detail'),
    path('listview/2-6/detail', views.detail, name = 'detail'),

    #살리기
    path('2-1/assignment', views.getAssignment2_1, name='assignment'),
    path('2-2/assignment', views.getAssignment2_2, name='assignment'),
    path('2-3/assignment', views.getAssignment2_3, name='assignment'),
    path('2-4/assignment', views.getAssignment2_4, name='assignment'),
    path('2-5/assignment', views.getAssignment2_5, name='assignment'),
    path('2-6/assignment', views.getAssignment2_6, name='assignment'),

    #살리기 - 학생일때 자기 반만 캘린더
    path('calendar',views.calendar, name='calendar'),

    #path('listview/',views.AssignmentList.as_view(), name='listview'),

    # path('calendar/2-1/', views.calendar2_1_stu, name='calendar2-1_stu'),
    # path('calendar/2-2/', views.calendar2_2_stu, name='calendar2-2_stu'),
    # path('calendar/2-3/', views.calendar2_3_stu, name='calendar2-3_stu'),


    #살리기
    path('2-1/', views.calendar2_1, name='calendar2-1'),
    path('2-2/', views.calendar2_2, name='calendar2-2'),
    path('2-3/', views.calendar2_3, name='calendar2-3'),
    path('2-4/', views.calendar2_4, name='calendar2-4'),
    path('2-5/', views.calendar2_5, name='calendar2-5'),
    path('2-6/', views.calendar2_6, name='calendar2-6'),



]




