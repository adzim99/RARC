from django.contrib import admin

# Register your models here.

from .models import Applicant, Booking, Feedback

admin.site.register(Applicant)
admin.site.register(Booking)
admin.site.register(Feedback)