from django.db import models
from shopping.models import Order

# Create your models here.

class ShippingProvider(models.Model):
    date_joined = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    transport_mode = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class DispenserCoolerBox(models.Model):
    box_number = models.IntegerField()
    location = models.CharField(max_length=50)
    unlock_code = models.IntegerField()

    def __str__(self):
        return self.location

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    shipping_provider = models.ForeignKey(ShippingProvider, on_delete=models.CASCADE)
    cooler_box = models.ForeignKey(DispenserCoolerBox, on_delete=models.CASCADE)

    def __str__(self):
        return self.dispatch_time


