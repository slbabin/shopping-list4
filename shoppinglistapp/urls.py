from django.urls import path
from .views import ShoppingList, ItemDetail


urlpatterns = [
    path('', ShoppingList.as_view(), name='shopping_list'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item_detail')
]
