from django.db import models

# Create your models here.

class Organization(models.Model):
    tin = models.CharField(max_length=12)
    name = models.CharField(max_length=255)
    registration_date = models.CharField(max_length=50)
    address = models.CharField(max_length=255)