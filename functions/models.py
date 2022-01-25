from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Applicant(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    matric_no = models.IntegerField(null=True)
    applicant_name = models.CharField(null=True, max_length=200)
    IC_no = models.IntegerField(null=True)
    student_tel_no = models.IntegerField(null=True)
    supervisor = models.CharField(null=True, max_length=200)
    staff_no = models.IntegerField(null=True)
    programme = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return str(self.matric_no)

class Booking(models.Model):
    L = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    S = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    STATS = (('Pending', 'Pending'),('Approved', 'Approved'),('Rejected', 'Rejected'),)

    applicant = models.ForeignKey(Applicant, null=True, on_delete=models.SET_NULL)

    laboratory_code = models.CharField(null=True, max_length=50)
    number_of_users = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    HI_work_activity = models.CharField(null=True, max_length=100)
    HI_hazard = models.CharField(null=True, max_length=100)
    HI_source = models.CharField(null=True, max_length=100)

    RA_existing_risk_control = models.CharField(null=True, max_length=100)
    RA_likelihood = models.IntegerField(null=True, validators=[MaxValueValidator(5),MinValueValidator(0)], choices=L)
    RA_severity = models.IntegerField(null=True, validators=[MaxValueValidator(5),MinValueValidator(0)], choices=S)
    RA_risk = models.IntegerField(null=True, validators=[MaxValueValidator(25),MinValueValidator(0)])

    RC_countermeasure = models.CharField(null=True, max_length=100)
    RC_PIC = models.CharField(null=True, max_length=100)

    booking_status = models.CharField(default="Pending", null=False, max_length=100, choices=STATS)
    remarks = models.CharField(default="-", null=False, max_length=200)

    def __str__(self):
        return str(self.HI_work_activity)

class ApplicantFeedback(models.Model):
    RATE = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    rating = models.IntegerField(null=True, choices=RATE)
    feedback = models.CharField(null=True, max_length=200)

    def __str__(self):
        return str(self.rating)