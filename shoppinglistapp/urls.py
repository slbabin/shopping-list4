from django.urls import path
from .views import ShoppingList, ItemDetail, ItemCreate, ItemUpdate, ItemDelete, AppLogin, AppRegister
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', AppLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', AppRegister.as_view(), name='register'),
    path('', ShoppingList.as_view(), name='shopping_list'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item'),
    path('item-create/', ItemCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>', ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>', ItemDelete.as_view(), name='item-delete')
]
