from lib2to3.pgen2.token import NAME
from sqlite3 import Date
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from winreg import REG_OPTION_VOLATILE
from django.db import models
from helpers.models import Tracking

class CustomUser(Tracking):
    First_name=models.CharField(max_length=255,default="")
    Last_name=models.CharField(max_length=255,default="")
    Other_names=models.CharField(max_length=255,default="")
    national_ID=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    Email=models.CharField(max_length=100,default="")
    Phone_number=models.CharField(max_length=255,default="")
    def __str__(self):
        return self.First_name+self.Last_name+self.Other_names
    class Meta:
        abstract = True
        ordering = ('-created_at',)

class Driver(CustomUser):
    license_no=models.CharField(max_length=255)
    license_expiry_date=models.DateField()
    def __str__(self):
         return self.First_name+self.Last_name+self.Other_names

class Vehicle_Owner(CustomUser):
    def __str__(self):
        return self.First_name+self.Last_name+self.Other_names

class Vehicle(Tracking):
    FUEL = (
        ('PETROL', 'PETROL'),
        ('DIESEL', 'DIESEL'),
    )
    V_TYPE = (
        ('TRUCK', 'TRUCK'),
        ('CONSTRUCTION', 'CONSTRUCTION'),
    )
    Reg_plate=models.CharField(max_length=100)
    make=models.CharField(max_length=255)
    color=models.CharField(max_length=255)
    Type_of_body=models.CharField(max_length=255)
    chasis_no=models.CharField(max_length=150)
    engine_no=models.CharField(max_length=150)
    year_of_manufacture=models.IntegerField(blank=False)
    carring_capacity=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=6, choices=FUEL)
    vehicle_type=models.CharField(max_length=12, choices=V_TYPE)
    millage=models.CharField(max_length=100)
    insuarance_expiry_date=models.IntegerField(blank=False)
    vehicle_owner=models.ForeignKey(to=Vehicle_Owner,on_delete=models.CASCADE,null=True)
    cost_per_km=models.IntegerField(blank=False)

    def __str__(self):
        return self.Reg_plate


class Tool(Tracking):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Staff(CustomUser):
    role=models.CharField(max_length=255)
    def __str__(self):
        return self.First_name+self.Last_name+self.Other_names

class Tool_issuing(Tracking):
    date=models.DateField()
    tool=models.ForeignKey(to=Tool, on_delete=models.CASCADE)
    driver=models.ForeignKey(to=Driver, on_delete=models.CASCADE)
    issuing_staff=models.ForeignKey(to=Staff, on_delete=models.CASCADE)
    comment=models.TextField()
    def __str__(self):
        return self.tool+self.driver

class Task(Tracking):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Booking(Tracking):
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    booking_date=models.DateField()
    start_date=models.DateField()
    end_date=models.DateField()
    security_deposit=models.IntegerField()
    allocated_staff=models.ForeignKey(to=Staff,on_delete=models.CASCADE)
    allocated_driver=models.ForeignKey(to=Vehicle,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(to=Driver,on_delete=models.CASCADE)
    purpose_of_the_journey=models.ForeignKey(to=Task,on_delete=models.CASCADE)
    def __str__(self):
        return self.booking_date

class Journey(Tracking):
    booking_id=models.ForeignKey(to=Booking,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    speedometer_reading_start=models.IntegerField()
    speedometer_reading_end=models.IntegerField()
    total_kms=models.IntegerField()
    fuel_consumed=models.IntegerField()
    engine_oil=models.IntegerField()
    other_oils=models.IntegerField()
    weight_carried=models.IntegerField()
    cost=models.IntegerField()
    def __str__(self):
        return self.booking_id

class Repair(Tracking):
    Registered_date=models.DateField()
    vehicle=models.ForeignKey(to=Driver,on_delete=models.CASCADE)
    issue=models.TextField()
    def __str__(self):
        return self.Registered_date