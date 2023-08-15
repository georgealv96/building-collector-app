from django.contrib import admin

# Register your models here.
from .models import Building, Visit

admin.site.register(Building)
admin.site.register(Visit)
