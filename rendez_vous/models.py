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

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    location_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField(null=True, blank=True)
    condition = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Horaire(models.Model):
    id_doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    location_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField(null=True, blank=True)
    condition = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    

class Assistant_Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    location_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField(null=True, blank=True)
    condition = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Rendez_vous(models.Model):
    id_doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    id_patient = models.ForeignKey(Patient,on_delete=models.PROTECT)
    location_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField(null=True, blank=True)
    condition = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
