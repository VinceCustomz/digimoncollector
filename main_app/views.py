from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Digimon, Pet
from .forms import PlaytimeForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# class Digimon:
#     def __init__(self, name, type, description, level):
#         self.name = name
#         self.type = type
#         self.description = description
#         self.level = level

# digimons = [
#     Digimon('Pattamon', 'flying', 'cute little guy', 10),
#     Digimon('Angelmon', 'Angel', 'Incredible', 50),
#     Digimon('Agumon', 'Dinosaur', 'breathes fire', 15)
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def digimons_index(request):
    digimons = Digimon.objects.filter(user=request.user)
    return render(request, 'digimons/index.html', {'digimons' : digimons})

@login_required
def digimons_details(request, digimon_id):
    digimon = Digimon.objects.get(id=digimon_id)
    # Get the pets that the digimon doesn't have
    pets_digimon_doesnt_have = Pet.objects.exclude(id__in = digimon.pets.all().values_list('id'))
    playtime_form = PlaytimeForm()
    return render(request, 'digimons/detail.html', {
        'digimon' : digimon, 'playtime_form': playtime_form, 
        # Add the pets to be displayed
        'pets': pets_digimon_doesnt_have
    })

@login_required
def add_playtime(request, digimon_id):
    form = PlaytimeForm(request.POST)
    if form.is_valid():
        new_playtime = form.save(commit=False)
        new_playtime.digimon_id = digimon_id
        new_playtime.save()
    return redirect('detail', digimon_id=digimon_id)

class PetList(LoginRequiredMixin, ListView):
    model = Pet

class PetDetail(LoginRequiredMixin, DetailView):
    model = Pet

class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    fields = '__all__'

class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['name', 'color']

class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/pets/'

class DigimonCreate(CreateView):
    model = Digimon
    fields = ['name', 'type', 'description', 'level']
    
    def form_valid(self, form):
        # this is done before django saves to the database
        form.instance.user = self.request.user
        # current logged in user, and then assign it
        return super().form_valid(form)

class DigimonUpdate(LoginRequiredMixin, UpdateView):
    model = Digimon
    fields = ['type', 'description', 'level']

class DigimonDelete(LoginRequiredMixin, DeleteView):
    model = Digimon
    success_url = '/pets/'

@login_required
def assoc_pet(request, digimon_id, pet_id):
    digimon = Digimon.objects.get(id=digimon_id)
    digimon.pets.add(pet_id)    
    return redirect('detail', digimon_id=digimon_id)

def unassoc_pet(request, digimon_id, pet_id):
    digimon = Digimon.objects.get(id=digimon_id)
    digimon.pets.remove(pet_id)    
    return redirect('detail', digimon_id=digimon_id)

# Create a 'user' form object; includes data from the broswer
def signup(request):
    error_message = ''
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # this adds user to database
            user = form.save()
            # this is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            eror_message = 'Invalid sign up - Try Again'
            # if its a bad POST or GET request, renders signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)