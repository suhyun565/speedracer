from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Manager)
admin.site.register(Product)
#admin.site.register(Inventory)
admin.site.register(Order)
