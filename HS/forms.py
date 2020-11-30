from django import forms
from .models import Assignment

class Assignmentform(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('title','subject','content','created','endline','author')