from django.contrib import admin
from . models import Room,Service,Booking
# Register your models here.
admin.site.register(Room)
admin.site.register(Service)
admin.site.register(Booking)
