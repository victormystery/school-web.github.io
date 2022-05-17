from distutils.command.upload import upload
from email.mime import image
from math import lgamma
from sre_parse import State
from django.db import models

# Create your models here.


class Gender(models.Model):
    gender = models.CharField(max_length=15)

    def __str__(self):
        return self.gender


class Child(models.Model):
    image = models.ImageField(
        width_field=80, height_field=50, upload_to='passport/', null=True)
    surname = models.CharField(max_length=50)
    other = models.CharField(max_length=150)
    DOB = models.DateField()
    LGA = models.CharField(max_length=150)
    State = models.CharField(max_length=150)
    Sex = models.ForeignKey(Gender, on_delete=models.CASCADE)
    Home_address = models.TextField()
    Previous_school = models.TextField(blank=True)
    Previous_class = models.CharField(max_length=50,null=True)
    from_duration = models.DateField()
    to_duration = models.DateField()
    father = models.CharField(max_length=250, null=True)
    occupation_father = models.CharField(max_length=250,null=True)
    mobile_father = models.IntegerField(null=True)
    email_father = models.EmailField(null=True)
    mother = models.CharField(max_length=250, null=True)
    occupation_mother = models.CharField(max_length=250,null=True)
    mobile_mother = models.IntegerField(null=True)
    email_mother = models.EmailField(null=True)
    immunized = models.BooleanField(null=True)
    medical_certificate = models.ImageField(upload_to='certify/', null=True)
    hearing_difficulty = models.BooleanField(null=True)
    doctor_consultation = models.BooleanField(null=True)
    Explain = models.TextField(blank=True)
    vision = models.BooleanField(null=True)
    spectacles = models.BooleanField(null=True)
    any_illness = models.BooleanField(null=True)
    description = models.TextField(blank=True)
