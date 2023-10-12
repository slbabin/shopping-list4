from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Item


class ShoppingList(ListView):
    model = Item
    context_object_name = 'items'


class ItemDetail(DetailView):
    model = Item
    context_object_name = 'item'


class ItemCreate(CreateView):
    model = Item
    # fields = ('user', 'name', 'notes', 'complete')
    fields = '__all__'  
    success_url = '/'
    # success_url = reverse_lazy('items')

