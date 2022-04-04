from tkinter import CASCADE
from django.db import models
from super_types.models import Super_type
# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=200)
    alter_ego = models.CharField(max_length=200)
    primary_ability = models.CharField(max_length=300)
    secondary_ability = models.CharField(max_length=300)
    catchphrase = models.CharField(max_length=300)
    super_type = models.ForeignKey(Super_type, on_delete=models.CASCADE)
