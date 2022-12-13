from django.db import models
from django.contrib.auth.models import User
# room-service-user===========================================
class Room(models.Model):
    name=models.CharField(max_length=200)
    no_of_bed=models.IntegerField()
    floor_no=models.IntegerField()
    space_in_square_ft=models.FloatField()
    price=models.FloatField()
    def __str_(self):
        return self.name
    class Meta:
        ordering = ['floor_no']

class Service(models.Model):
    name=models.CharField(max_length=200)
    def __str_(self):
        return self.name
    class Meta:
        ordering = ['name']





# booking - room_has_service===========================================

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True,blank=True)
    from_date = models.DateField()
    to_date =models.DateField()