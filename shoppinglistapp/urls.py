from django.urls import path
from . import views


urlpatterns = [
    path('', views.shoppingList, name='shopping_list')
]
