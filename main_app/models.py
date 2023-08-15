from django.db import models
from django.urls import reverse

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)
    opening_year = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    height_in_feet = models.FloatField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'building_id': self.id})
    