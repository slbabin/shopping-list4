from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Item


class ShoppingList(ListView):
    model = Item
    context_object_name = 'items'


class ItemDetail(DetailView):
    model = Item
    context_object_name = 'item_detail'
    # template_name = 'shoppingapplistapp/detail.html'

