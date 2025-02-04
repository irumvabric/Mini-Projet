from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import User,Doctor,Patient,Availability,Assistant_Doctor,Rendez_vous
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','password','is_active','is_staff', 'confirm']
        read_only_fields = ['id','is_active','is_staff']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

class PatientsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = Patient
        fields = '__all__'

    def update(self, instance, validated_data):
        # Use `.get()` to prevent overwriting existing values with None
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Doctor
        fields = '__all__'
    
   

class AvailabilitySerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only = True)

    class Meta:
        model = Availability
        fields = '__all__'

   
class Assistant_DoctorSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only = True)

    class Meta:
        model = Assistant_Doctor
        fields = '__all__'


class Rendez_vousSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only = True)
    patient = PatientsSerializer(read_only = True)
    class Meta:
        model = Rendez_vous
        fields = '__all__'

    