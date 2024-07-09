from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

class Cat(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    vaccination_status = models.BooleanField(default=True)

class Booking(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Confirmed')
