from django.db import models
from django.contrib.auth.models import User
from functions.models import Booking

# Create your models here.

class Office(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    staff_no = models.IntegerField(null=True)
    staff_name = models.CharField(null=True, max_length=200)
    designation = models.CharField(null=True, max_length=100)
    tel_no = models.IntegerField(null=True)

    def __str__(self):
        return str(self.staff_no)

class OfficeFeedback(models.Model):
    RATE = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    rating = models.IntegerField(null=True, choices=RATE)
    feedback = models.CharField(null=True, max_length=200)

    def __str__(self):
        return str(self.rating)        