from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class BuildingCreate(CreateView):
    model = Building
    fields = '__all__'

class BuildingUpdate(UpdateView):
    model = Building
    fields = '__all__'

class BuildingDelete(DeleteView):
    model = Building
    success_url = '/buildings'