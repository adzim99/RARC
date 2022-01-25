from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        exclude = ['user']

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['applicant', 'delete', 'booking_status', 'remarks']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ApplicantFeedbackForm(forms.ModelForm):
    class Meta:
        model = ApplicantFeedback
        fields = '__all__'