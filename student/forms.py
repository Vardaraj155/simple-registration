from django import forms
from django.contrib.auth.forms import UserCreationForm
from student.models import Student


class registration(UserCreationForm):
    username = forms.CharField(max_length=30, help_text="Username should not conain special character")
    class Meta:
        model = Student
        fields = ("username","Email", "Department","password1","password2")
