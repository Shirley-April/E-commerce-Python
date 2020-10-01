from django.contrib import admin
from django.urls import path
from .views import products_list, product_details, upload_products

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", products_list, name="products_list"),
    path("products/<int:product_id>/", product_details, name="details"),
    path("products/upload/", upload_products, name="uploads")
]
