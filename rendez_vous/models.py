from django.db import models
from django.contrib.auth.models import User

class UserRoleConst(models.TextChoices):
    Doctor = "Doctor"
    Assisant = "Assisant"
    Patient = "Patient"

class GenderConst(models.TextChoices):
    Male = "M"
    Female = "F"

class AvailabilityConst(models.TextChoices):
    Available = "Available"
    Busy = "Busy"

class Rendez_vousConst(models.TextChoices):
    Pending = "Pending"
    Confirmed = "Confirmed"
    Canceled = "Canceled"
     

class User(User):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    # email = models.EmailField(max_length=70,unique=True)
    # password = models.CharField(max_length=100)
    role = models.CharField(max_length=10,choices=UserRoleConst,default=UserRoleConst.Patient)
    

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=GenderConst,default=GenderConst.Male)
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    speciality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=GenderConst,default=GenderConst.Male)
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Availability(models.Model):
    id_doctor = models.ForeignKey(Doctor,max_length=255,on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10,choices=AvailabilityConst,default=AvailabilityConst.Busy)

    def __str__(self):
        return self.name

    

class Assistant_Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=GenderConst,default=GenderConst.Male)
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
    status = models.CharField(max_length=10,choices=Rendez_vousConst,default=Rendez_vousConst.Pending)

    def __str__(self):
        return self.name
