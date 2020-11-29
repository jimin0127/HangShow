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

