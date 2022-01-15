from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
from functions.models import Booking

class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = '__all__'
        exclude = ['user']

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OfficeFeedbackForm(forms.ModelForm):
    class Meta:
        model = OfficeFeedback
        fields = '__all__'