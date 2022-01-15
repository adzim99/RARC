from django.contrib import admin

# Register your models here.

from .models import Office, OfficeFeedback

admin.site.register(Office)
admin.site.register(OfficeFeedback)