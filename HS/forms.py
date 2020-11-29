from django import forms
from .models import Assignment

class Assignment(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('subject','content',)