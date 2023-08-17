from django.contrib import admin

# Register your models here.
from .models import Building, Visit, Reference, Photo

admin.site.register(Building)
admin.site.register(Visit)
admin.site.register(Reference)
admin.site.register(Photo)
