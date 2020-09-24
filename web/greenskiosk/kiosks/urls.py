from django.urls import path
from .views import upload_kiosk
from catalogue.views import upload_products

urlpatterns = [
    path('kiosks/upload/', upload_kiosk, name='kiosk_uploads'),
    path("products/upload/", upload_products, name="uploads")
]