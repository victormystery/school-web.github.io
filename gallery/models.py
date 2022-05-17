from distutils.command.upload import upload
from turtle import mode
from django.db import models

# Create your models here.
class Image(models.Model):
    image_file = models.ImageField(width_field=None, upload_to = None, height_field= None)