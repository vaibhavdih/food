from django.db import models
from datetime import date


class Bookings(models.Model):
    slot_date=models.CharField(max_length=25)
    donate_address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    slot_time = models.CharField(max_length=20)
    organisation_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    email_address = models.CharField(max_length=50)
    no_packets = models.IntegerField(default=0)
    request_date = models.DateField(default=date.today)
    request_time = models.TimeField(auto_now_add=True)
