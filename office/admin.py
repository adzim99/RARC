from django.contrib import admin

# Register your models here.

from .models import Office, Feedback

admin.site.register(Office)
admin.site.register(Feedback)