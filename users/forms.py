from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model  = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:

        model  = User
        fields = ['username', 'email']

        name = User.objects.all()


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model  = Profile
        fields = ['profile_pic']


class UserDeleteForm(forms.ModelForm):

    class Meta:

        model  = User
        fields = []
