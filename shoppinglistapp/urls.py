from django.urls import path
from .views import ShoppingList


urlpatterns = [
    path('', ShoppingList.as_view(), name='shopping_list')
]
