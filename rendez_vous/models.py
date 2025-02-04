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
    # id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    # email = models.EmailField(max_length=70,unique=True)
    # password = models.CharField(max_length=100)
    role = models.CharField(max_length=10,choices=UserRoleConst,default=UserRoleConst.Patient)
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=GenderConst,default=GenderConst.Male)
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    speciality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=GenderConst,default=GenderConst.Male)
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor,max_length=255,on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10,choices=AvailabilityConst,default=AvailabilityConst.Busy)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Assistant - {self.doctor}"

    

class Assistant_Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=GenderConst,default=GenderConst.Male)
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100) 
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        db_table='assistant_doctor'
        ordering = ['created']
        verbose_name = 'assistant_doctor'
        verbose_name_plural = 'assistants_doctor'


    

class Rendez_vous(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient,on_delete=models.PROTECT)
    date = models.DateField()
    description = models.TextField()
    heure_arrive = models.TimeField()
    heure_fin = models.TimeField()
    status = models.CharField(max_length=10,choices=Rendez_vousConst,default=Rendez_vousConst.Pending)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"RDV - {self.doctor} {self.patient} {self.date} {self.status}"
