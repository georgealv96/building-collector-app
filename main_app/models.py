from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Reference(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('references_index')

class Building(models.Model):
    name = models.CharField(max_length=100)
    opening_year = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    height_in_feet = models.FloatField()
    # M:M relationship
    references = models.ManyToManyField(Reference)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'building_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for building_id: {self.building_id} @{self.url}'

RATINGS = (
    ('G', 'Good'),
    ('O', 'Okay'),
    ('B', 'Bad')
)

class Visit(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Visit Date')
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[1][0])
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_rating_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']