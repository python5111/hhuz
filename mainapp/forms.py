from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    model = User
    fields=['username','email','password1','password2']

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model =Job_creat
        fields = '__all__'
    