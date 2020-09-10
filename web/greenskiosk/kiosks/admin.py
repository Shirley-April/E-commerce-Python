from django.contrib import admin
from .models import KioskOwner, Kiosk

# Register your models here.

admin.site.register(Kiosk)
admin.site.register(KioskOwner)
