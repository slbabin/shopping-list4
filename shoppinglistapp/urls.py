from django.urls import path
from .views import ShoppingList, ItemDetail, ItemCreate, ItemUpdate, ItemDelete, AppLogin


urlpatterns = [
    path('login/', AppLogin, name='login'),
    path('', ShoppingList.as_view(), name='shopping_list'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item'),
    path('item-create/', ItemCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>', ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>', ItemDelete.as_view(), name='item-delete')
]
