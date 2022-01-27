from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

import calculation

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        exclude = ['user']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['booking_status', 'remarks']

        widgets = {
            'RA_risk':calculation.FormulaInput('RA_likelihood*RA_severity')
        }
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ApplicantFeedbackForm(forms.ModelForm):
    class Meta:
        model = ApplicantFeedback
        fields = '__all__'