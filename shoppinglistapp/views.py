from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Item


class AppLogin(LoginView):
    template_name = 'shoppinglistapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('shopping_list')


class AppRegister(FormView):
    template_name = 'shoppinglistapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('shopping_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(AppRegister,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('shopping_list')
        return super(AppRegister, self).get(*args, **kwargs) 


class ShoppingList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user) # Make sure user can get their own data
        context['count'] = context['items'].filter().count()
        return context



class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = 'item'


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ('name', 'notes', 'complete')
    # fields = '__all__'
    success_url = reverse_lazy('shopping_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('shopping_list')


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ('name', 'notes', 'complete')
    success_url = reverse_lazy('shopping_list')
