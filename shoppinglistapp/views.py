from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Item


class ShoppingList(ListView):
    model = Item

