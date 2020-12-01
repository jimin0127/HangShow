
from django.contrib import auth
from datetime import timezone
from django.shortcuts import render, redirect
from .forms import Assignmentform
from .models import *
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import Assignment
from django.views.generic import ListView
from .models import Assignment

class AssignmentList(ListView):
    model=Assignment

    def get_queryset(self):
        return Assignment.objects.order_by('-created')

def calendar(request):
    assignment=Assignment.objects.all()
    return render(
        request,
        'HS/calendar.html',
        {
            'assignments':assignment,
        }
    )

def calendar2_1(request):
    assignment=class_2_1.objects.all()
    return render(
        request,
        'HS/calendar.html',
        {
            'assignments':assignment,
        }
    )

def calendar2_2(request):
    assignment=class_2_2.objects.all()
    return render(
        request,
        'HS/calendar.html',
        {
            'assignments':assignment,
        }
    )

def calendar2_3(request):
    assignment=class_2_3.objects.all()
    return render(
        request,
        'HS/calendar.html',
        {
            'assignments':assignment,
        }
    )

def index(request):
    return render(
        request,
        'HS/index.html'
    )


def getAssignment(request):
    if request.method=="POST":
        form=Assignmentform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'HS/getassignment.html', {'form': form})
    else:
        form = Assignmentform()
        return render(request, 'HS/getassignment.html', {'form': form})


def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'HS/account.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'HS/account.html', {'form': form})


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print(name)

        user = auth.authenticate(request, name=name, password=password)

        if user is not None: # 로그인에 성공하면
            auth.login(request, user)
            return render(request, 'HS/calendar.html',{})
        else:
            return render(request, 'HS/index.html', {'error': '에러'}) # 로그인 실패
    else:
        print("login2")
        return render(request, 'HS/login.html', {'error': '에러'})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'HS/index.html', {'error': '에러'})
    else:
        auth.logout(request)
        return render(request, 'HS/index.html', {'error': '에러'})