from distutils.command.upload import upload
from email.policy import default
from re import T
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='eze ayo azaki(Default)', max_length=200, null=True)
    title = models.CharField(default='', max_length=200, null=True)
    desc_text = '', 
    desc = models.CharField(default= desc_text, max_length=200, null=True)
    profile_img = models.ImageField(default='', upload_to='images', null=True, blank = True)
    
    def __str__(self):
        return self.name


# class Data(models.Model):
#     surname = models.CharField(max_length=150)
#     other_name = models.CharField(max_length=200)
#     Date_of_Birth = models.DateField()
#     LGA = models.CharField(max_length=200)
#     State = models.CharField(max_length=200)
#     sex = models.CharField(max_length=50)
#     address = models.TextField()
#     previous_school = models.CharField(max_length=500)
    

