from datetime import timezone
from django.shortcuts import render, redirect
from .forms import Assignmentform
from .models import *
from .forms import UserCreationForm
from django.shortcuts import render
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

