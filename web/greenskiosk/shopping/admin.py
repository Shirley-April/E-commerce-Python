from django.contrib import admin
from .models import Payment, Order, Cart
# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)
