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

def assignment(request):
    form = Assignment()
    return render(request, 'HS/assignment.html', {'form': form})

# def index(request):
#     assignments=Assignment.objects.all()
#
#     return render(
#         request,
#         'HS/assignment_list.html',
#         {
#              'assignments':assignments,
#         }
#     )
# Create your views here.
def index(request):
    return render(
        request,
        'HS/account.html'
    )

def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'HS/account.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'HS/account.html', {'form': form})

