from django.urls import path
from .views import ShoppingList, ItemDetail, ItemCreate, ItemUpdate


urlpatterns = [
    path('', ShoppingList.as_view(), name='shopping_list'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item'),
    path('item-create/', ItemCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>', ItemUpdate.as_view(), name='item-update')
]
