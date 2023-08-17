from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Building, Reference
from .forms import VisitForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def buildings_index(request):
    # This reads ALL buildings, not just the logged in user's buildings
    # buildings = Building.objects.all()

    buildings = Building.objects.filter(user=request.user)
    return render(request, 'buildings/index.html', {
        'buildings': buildings
    })

@login_required
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

class BuildingCreate(LoginRequiredMixin, CreateView):
    model = Building
    fields = ['name', 'opening_year', 'city', 'country', 'height_in_feet']

    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class BuildingUpdate(LoginRequiredMixin, UpdateView):
    model = Building
    fields = '__all__'

class BuildingDelete(LoginRequiredMixin, DeleteView):
    model = Building
    success_url = '/buildings'

@login_required
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

@login_required
def assoc_reference(request, building_id, reference_id):
    Building.objects.get(id=building_id).references.add(reference_id)
    return redirect('detail', building_id=building_id)

class ReferenceList(LoginRequiredMixin, ListView):
    model = Reference

class ReferenceCreate(LoginRequiredMixin, CreateView):
    model = Reference
    fields = '__all__'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with and empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)