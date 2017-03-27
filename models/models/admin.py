from django.contrib import admin

from .models import User, Sellers, Buyers, Car, Authenticator

admin.site.register(User)
admin.site.register(Sellers)
admin.site.register(Buyers)
admin.site.register(Car)
admin.site.register(Authenticator)

# Register your models here.
