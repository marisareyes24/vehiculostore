from django.contrib import admin
from .models import Vehicle

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model','year', 'price', 'image']

admin.site.register(Vehicle,VehicleAdmin)