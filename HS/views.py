from django.contrib import auth
from datetime import timezone
from django.shortcuts import render, redirect
from .forms import *
from .models import class_2_1
from .models import *
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import Assignment
from django.views.generic import ListView
from .models import Assignment


class AssignmentList(ListView):
    model = Assignment

    def get_queryset(self):
        return Assignment.objects.order_by('-created')

def AssignmentList(request):
    assignmentList = AssignmentList.objects.all()
    return render(
        request,
        'HS/assignment_list.html',
        {
            'assignmentList': assignmentList,
        }
    )

def AssignmentList2_1(request):
    assignmentList = class_2_1.objects.all()
    return render(
        request,
        'HS/assignment_list.html',
        {
            'assignmentList': assignmentList,
        }
    )

def AssignmentList2_2(request):
    assignmentList = class_2_2.objects.all()
    return render(
        request,
        'HS/assignment_list.html',
        {
            'assignmentList': assignmentList,
        }
    )

def AssignmentList2_3(request):
    assignmentList = class_2_3.objects.all()
    return render(
        request,
        'HS/assignment_list.html',
        {
            'assignmentList': assignmentList,
        }
    )

def AssignmentList2_4(request):
    assignmentList = class_2_4.objects.all()
    return render(
        request,
        'HS/assignment_list.html',
        {
            'assignmentList': assignmentList,
        }
    )

def AssignmentList2_5(request):
    assignmentList = class_2_5.objects.all()
    return render(
        request,
        'HS/assignment_list.html',
        {
            'assignmentList': assignmentList,
        }
    )

def AssignmentList2_6(request):
    assignmentList = class_2_6.objects.all()
    return render(
        request,
        'HS/assignment_list.html',
        {
            'assignmentList': assignmentList,
        }
    )


def detail(request):
    if request.method == "GET":
        title = request.GET['title']
        author = request.GET['author']
        created = request.GET['created']
        content = request.GET['content']
        print(title)

        return render(request,
                      'HS/detail.html',
                      {'title': title,
                       'author':author,
                       'created':created,
                       'content':content
                       }

                      )
    else:
        return render(request, 'HS/index.html', {})




# calendar views
def calendar(request):
    assignment = Assignment.objects.all()
    return render(
        request,
        'HS/calendartea.html',
        {
            'assignments': assignment,
        }
    )


def calendar2_1(request):
    assignment = class_2_1.objects.all()
    return render(
        request,
        'HS/calendartea.html',
        {
            'assignments': assignment,
        }
    )


def calendar2_2(request):
    assignment = class_2_2.objects.all()
    return render(
        request,
        'HS/calendartea.html',
        {
            'assignments': assignment,
        }
    )


def calendar2_3(request):
    assignment = class_2_3.objects.all()
    return render(
        request,
        'HS/calendartea.html',
        {
            'assignments': assignment,
        }
    )

def calendar2_4(request):
    assignment = class_2_4.objects.all()
    return render(
        request,
        'HS/calendartea.html',
        {
            'assignments': assignment,
        }
    )

def calendar2_5(request):
    assignment = class_2_5.objects.all()
    return render(
        request,
        'HS/calendartea.html',
        {
            'assignments': assignment,
        }
    )

def calendar2_6(request):
    assignment = class_2_6.objects.all()
    return render(
        request,
        'HS/calendartea.html',
        {
            'assignments': assignment,
        }
    )


def index(request):
    return render(
        request,
        'HS/index.html'
    )


# assignment views
def getAssignment(request):
    if request.method == "POST":
        form = Assignmentform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'HS/getassignment.html', {'form': form})
    else:
        form = Assignmentform()
        return render(request, 'HS/getassignment.html', {'form': form})


def getAssignment2_1(request):
    if request.method == "POST":
        form = Assignmentform2_1(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'HS/getassignment.html', {'form': form})
    else:
        form = Assignmentform2_1()
        return render(request, 'HS/getassignment.html', {'form': form})


def getAssignment2_2(request):
    if request.method == "POST":
        form = Assignmentform2_2(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'HS/getassignment.html', {'form': form})
    else:
        form = Assignmentform2_2()
        return render(request, 'HS/getassignment.html', {'form': form})


def getAssignment2_3(request):
    if request.method == "POST":
        form = Assignmentform2_3(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'HS/getassignment.html', {'form': form})
    else:
        form = Assignmentform2_3()
        return render(request, 'HS/getassignment.html', {'form': form})


def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'HS/login.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'HS/account.html', {'form': form})


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print(name)

        user = auth.authenticate(request, name=name, password=password)

        if user is not None:  # 로그인에 성공하면
            if name == "hhy":
                auth.login(request, user)
                return render(request, 'HS/calendartea.html', {})
            else:
                auth.login(request, user)
                return render(request, 'HS/calendarstu.html', {})
        else:
            return render(request, 'HS/index.html', {'error': '에러'})  # 로그인 실패
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
