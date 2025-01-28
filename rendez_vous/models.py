from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    location_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField(null=True, blank=True)
    condition = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)



