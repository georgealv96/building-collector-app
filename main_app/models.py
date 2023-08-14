from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)
    opening_year = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    height_in_feet = models.FloatField()
    