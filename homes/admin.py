from django.contrib import admin

from homes.models import ApartmentRent, ApartmentSale, Room

admin.site.register(ApartmentRent)
admin.site.register(ApartmentSale)
admin.site.register(Room)
