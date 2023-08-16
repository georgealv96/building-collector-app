from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

# Create your views here.
from .models import Building, Reference
from .forms import VisitForm

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
    # Get the references the building doesn't have
    id_list = building.references.all().values_list('id')
    references_building_doesnt_have = Reference.objects.exclude(id__in=id_list)
    # instantiate VisitForm to be rendered in the template
    visit_form = VisitForm()
    # include the building and visit_form in the context
    return render(request, 'buildings/detail.html', { 
        'building': building,
        'visit_form': visit_form,
        'references': references_building_doesnt_have
    })

class BuildingCreate(CreateView):
    model = Building
    fields = ['name', 'opening_year', 'city', 'country', 'height_in_feet']

class BuildingUpdate(UpdateView):
    model = Building
    fields = '__all__'

class BuildingDelete(DeleteView):
    model = Building
    success_url = '/buildings'

def add_visit(request, building_id):
    # create a ModelForm instance using the data in request.POST (req.body in Express.js)
    form = VisitForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't dave the form to the db until it
        # has the building_id assigned
        new_visit = form.save(commit=False)
        new_visit.building_id = building_id
        new_visit.save()
    return redirect('detail', building_id=building_id)

class ReferenceList(ListView):
    model = Reference

class ReferenceCreate(CreateView):
    model = Reference
    fields = '__all__'
