from django.contrib import admin
from .models import BodyType, Car, Rental

# Register your models here.
admin.site.register(BodyType)
admin.site.register(Car)
admin.site.register(Rental)