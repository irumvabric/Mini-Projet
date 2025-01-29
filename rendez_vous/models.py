from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    horaire = models.ForeignKey(Horaire,on_delete=models.PROTECT)
    gender = models.enums('M','F')
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Horaire(models.Model):
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
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    horaire = models.ForeignKey(Horaire,on_delete=models.PROTECT)
    gender = models.enums('M','F')
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    


class Assistant_Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.enums('M','F')
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Rendez_vous(models.Model):
    id_doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    id_patient = models.ForeignKey(Patient,on_delete=models.PROTECT)
    date = models.DateField()
    description = models.TextField()
    heure_arrive = models.TimeField()
    heure_fin = models.TimeField()
    status = models.enums('pending','confirmed','canceled')

    def __str__(self):
        return self.name
