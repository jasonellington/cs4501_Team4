from django.contrib import admin

from .models import User, Sellers, Buyers, Car

admin.site.register(User)
admin.site.register(Sellers)
admin.site.register(Buyers)
admin.site.register(Car)

# Register your models here.
