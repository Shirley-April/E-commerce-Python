from django.db import models
from catalogue.models import Product
from customers.models import Customer
# from shipping.models import ShippingProvider

# Create your models here.

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    date_created = models.DateTimeField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)   
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    # shipping_provider = models.ForeignKey(ShippingProvider, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=5, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.order_price



class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method =  models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_Payment = models.DateTimeField()

    def __str__(self):
        return self.order



    

         
