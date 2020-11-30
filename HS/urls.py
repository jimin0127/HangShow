from django.urls import path, include
from . import views

urlpatterns = [
    path('assignment/', views.getAssignment, name='assignment'),
    path('calendar/',views.calendar, name='calendar'),
    path('listview/',views.AssignmentList.as_view(), name='listview'),

    path('',views.index),
]




