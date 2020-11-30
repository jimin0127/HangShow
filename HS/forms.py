from django import forms
from .models import User
from django.utils.translation import ugettext_lazy as _
from .models import Assignment

class UserCreationForm(forms.ModelForm):
    id = forms.CharField()
    name = forms.CharField()
    student_id = forms.CharField(max_length=4)
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('id', 'name', 'student_id', 'email', 'password')


class Assignmentform(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('title','subject','content','created','endline','author')