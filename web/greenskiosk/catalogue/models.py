from django.db import models
from django.contrib.auth.models import User
from kiosks.models import Kiosk
from customers.models import Customer
# Create your models here.

class ProductSupplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    street_address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    id_number = models.IntegerField()
    date_added = models.DateField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.street_address
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    category= models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField()
    supplier_price = models.DecimalField(max_digits=5, decimal_places=2)
    selling_price = models.DecimalField(max_digits=5, decimal_places=2)
    supplier = models.ForeignKey(ProductSupplier, on_delete=models.CASCADE)
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE)
    number_in_stock = models.IntegerField()
    
    product_image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        return self.review
    
    