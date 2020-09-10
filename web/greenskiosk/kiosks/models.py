from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class KioskOwner(models.Model):
    GENDERS = (
        ("m", "male"),
        ("f", "female")
    )
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.gender

class Kiosk(models.Model):
    owner = models.ForeignKey(KioskOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date_opened =  models.DateField()
    street_address = models.CharField(max_length=8)
    currency = models.CharField(max_length=8)
    phone_number = models.IntegerField()
    business_type =models.CharField(max_length=20)

    def __str__(self):
        return self.name
    