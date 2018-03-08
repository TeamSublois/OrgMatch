from django.contrib.auth.models import User
from .models import Volunteer
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class VolunteerForm(forms.ModelForm):
    class Meta():
        model = Volunteer
        fields = ('bio', 'profile_picture', 'city', 'state', 'category_list',
                  'profile_picture')
