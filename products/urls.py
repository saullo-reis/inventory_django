from django.urls import path
from .views import list_products, add_product, edit_product, delete_product

urlpatterns = [
    path('', list_products, name='list'),
    path('add/', add_product, name='add'),
    path('edit/<int:pk>/', edit_product, name='edit'),
    path('delete/<int:pk>/', delete_product, name='delete'),
]
