from django.urls import path
from .views import products_list, products_details

urlpatterns = [
    path('', products_list, name='products-list'),
    path('products/<int:product_id>/', products_details, name='products_details')
]