from django.contrib import admin
from . import models
from django.contrib.admin import AdminSite

admin.site.register(models.User)
admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Availability)
admin.site.register(models.Assistant_Doctor)
admin.site.register(models.Rendez_vous)
