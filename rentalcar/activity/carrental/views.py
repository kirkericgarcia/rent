from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from carrental.models import Rental
from carrental.forms import RentalForm  

# Create your views here.
class RentListView(ListView):
    template_name = 'index.html'
    model = Rental
    queryset = Rental.objects.all()
    context_object_name = 'rent_list'

class RentDetailView(DetailView):
    model = Rental
    template_name = 'rent_detail.html'
    context_object_name = 'rent'

class RentCreateView(CreateView):
    form_class = RentalForm  
    model = Rental 
    template_name = 'rent_create.html'
    success_url = '/carrental/'

class RentUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rent_update.html'
    context_object_name = 'rent'
    success_url = '/carrental/'
    
class RentDeleteView(DeleteView):
    template_name = 'rent_confirm_delete.html'
    context_object_name = 'rent'
    model = Rental
    success_url = '/carrental/'