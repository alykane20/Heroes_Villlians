from tkinter import CASCADE
from django.db import models
from super_types.models import Super_type
# Create your models here.

class Power(models.Model):
    name = models.CharField(max_length=200)

class Super(models.Model):
    name = models.CharField(max_length=200)
    alter_ego = models.CharField(max_length=200)
    powers = models.ManyToManyField(Power)
    catchphrase = models.CharField(max_length=300)
    super_type = models.ForeignKey(Super_type, on_delete=models.CASCADE)


