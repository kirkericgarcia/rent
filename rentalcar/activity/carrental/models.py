from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Car(models.Model):
    car_type = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    renters = models.ManyToManyField(User, through='Rental', related_name='renter')

class Rental(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_rent = models.DateTimeField()
    end_rent = models.DateTimeField()
    cost = models.IntegerField(default=0)
