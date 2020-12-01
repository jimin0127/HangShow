from django import forms
from django.forms import widgets

from .models import User
from django.utils.translation import ugettext_lazy as _
from .models import Assignment
from .models import class_2_1
from .models import class_2_2
from .models import class_2_3

class UserCreationForm(forms.ModelForm):
    id = forms.CharField()
    name = forms.CharField()
    student_id = forms.CharField(max_length=4)
    email = forms.EmailField()
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'student_id', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class Assignmentform(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'subject', 'content', 'created', 'endline', 'author')

class Assignmentform2_1(forms.ModelForm):
    class Meta:
        model = class_2_1
        fields = ('title', 'subject', 'content', 'created', 'endline', 'author')

class Assignmentform2_2(forms.ModelForm):
    class Meta:
        model = class_2_2
        fields = ('title', 'subject', 'content', 'created', 'endline', 'author')

class Assignmentform2_3(forms.ModelForm):
    class Meta:
        model = class_2_3
        fields = ('title', 'subject', 'content', 'created', 'endline', 'author')
