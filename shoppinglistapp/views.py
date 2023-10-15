from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item


class AppLogin(LoginView):
    template_name = 'shoppinglistapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('shopping_list')


class ShoppingList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'


class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = 'item'


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    # fields = ('user', 'name', 'notes', 'complete')
    fields = '__all__'
    success_url = reverse_lazy('shopping_list')


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('shopping_list')


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('shopping_list')
