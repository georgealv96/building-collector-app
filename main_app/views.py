from django.shortcuts import render

# Create your views here.
from .models import Building

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def buildings_index(request):
    
    buildings = Building.objects.all()

    return render(request, 'buildings/index.html', {
        'buildings': buildings
    })

def buildings_detail(request, building_id):
    
    building = Building.objects.get(id=building_id)

    return render(request, 'buildings/detail.html', { 'building': building 
    })