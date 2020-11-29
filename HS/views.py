from django.shortcuts import render, redirect
from .models import *
from .forms import UserCreationForm


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

