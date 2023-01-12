from lib2to3.pgen2.token import NAME
from sqlite3 import Date
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from winreg import REG_OPTION_VOLATILE
from django.db import models
from helpers.models import Tracking

class CustomUser(Tracking):
    FIRST_NAME=models.CharField(max_length=255,default=True)
    LAST_NAME=models.CharField(max_length=255,default=True)
    OTHER_NAMES=models.CharField(max_length=255,default=True)
    NATIONAL_ID=models.CharField(max_length=100,default=True)
    ADDRESS=models.CharField(max_length=100,default=True)
    EMAIL=models.CharField(max_length=100,default=True)
    PHONE_NUMBER=models.CharField(max_length=255,default=True)
    def __str__(self):
        return self.FIRST_NAME+self.LAST_NAME+self.OTHER_NAMES
    class Meta:
        abstract = True
        ordering = ('-created_at',)

class Driver(CustomUser):
    LICENSE_NO=models.CharField(max_length=255)
    LICENSE_EXPIRY_DATE=models.DateField()
    def __str__(self):
        return self.FIRST_NAME+self.LAST_NAME+self.OTHER_NAMES

class Vehicle_Owner(CustomUser):
    def __str__(self):
        return self.FIRST_NAME+self.LAST_NAME+self.OTHER_NAMES

class Vehicle(Tracking):
    FUEL = (
        ('PETROL', 'PETROL'),
        ('DIESEL', 'DIESEL'),
    )
    V_TYPE = (
        ('TRUCK', 'TRUCK'),
        ('CONSTRUCTION', 'CONSTRUCTION'),
    )
    REG_PLATE=models.CharField(max_length=100)
    MAKE=models.CharField(max_length=255)
    COLOR=models.CharField(max_length=255)
    TYPE_OF_BODY=models.CharField(max_length=255)
    CHASIS_NO=models.CharField(max_length=150)
    ENGINE_NO=models.CharField(max_length=150)
    YEAR_OF_MANUFACTURE=models.IntegerField(blank=False)
    CARRING_CAPACITY=models.CharField(max_length=100)
    FUEL_TYPE=models.CharField(max_length=6, choices=FUEL)
    VEHCILE_TYPE=models.CharField(max_length=12, choices=V_TYPE)
    MILLAGE=models.CharField(max_length=100)
    INSUARANCE_EXPIRY_DATE=models.IntegerField(blank=False)
    VEHICLE_OWNER=models.ForeignKey(to=Vehicle_Owner,on_delete=models.CASCADE)
    COST_PER_KM=models.IntegerField(blank=False)

    def __str__(self):
        return self.REG_PLATE


class Tool(Tracking):
    NAME=models.CharField(max_length=100)
    DESCRIPTION=models.TextField(blank=True)

    def __str__(self):
        return self.NAME

class Staff(CustomUser):
    ROLE=models.CharField(max_length=255)
    def __str__(self):
        return self.FIRST_NAME+self.LAST_NAME+self.OTHER_NAMES

class Tool_issuing(Tracking):
    DATE=models.DateField()
    TOOL=models.ForeignKey(to=Tool, on_delete=models.CASCADE)
    DRIVER=models.ForeignKey(to=Driver, on_delete=models.CASCADE)
    ISSUING_STAFF=models.ForeignKey(to=Staff, on_delete=models.CASCADE)
    COMMENT=models.TextField()
    def __str__(self):
        return self.TOOL+self.DRIVER

class Task(Tracking):
    NAME=models.CharField(max_length=100)
    DESCRIPTION=models.TextField(blank=True)
    def __str__(self):
        return self.NAME

class Booking(Tracking):
    SOURCE=models.CharField(max_length=100)
    DESTINATION=models.CharField(max_length=100)
    BOOKING_DATE=models.DateField()
    START_DATE=models.DateField()
    END_DATE=models.DateField()
    SECURITY_DEPOSIT=models.IntegerField()
    ALLOCATED_STAFF=models.ForeignKey(to=Staff,on_delete=models.CASCADE)
    ALLOCATED_DRIVER=models.ForeignKey(to=Vehicle,on_delete=models.CASCADE)
    VEHICLE=models.ForeignKey(to=Driver,on_delete=models.CASCADE)
    PURPOSE_OF_THE_JOURNEY=models.ForeignKey(to=Task,on_delete=models.CASCADE)
    def __str__(self):
        return self.BOOKING_DATE

class Journey(Tracking):
    BOOKING_ID=models.ForeignKey(to=Booking,on_delete=models.CASCADE)
    START_DATE=models.DateField()
    END_DATE=models.DateField()
    SPEEDOMETER_READING_START=models.IntegerField()
    SPPEDOMETER_READING_END=models.IntegerField()
    TOTAL_KMS=models.IntegerField()
    FUEL_CONSUMED=models.IntegerField()
    ENGINE_OIL=models.IntegerField()
    OTHER_OILS=models.IntegerField()
    WEIGHT_CARRIED=models.IntegerField()
    COST=models.IntegerField()
    def __str__(self):
        return self.BOOKING_ID

class Repair(Tracking):
    REGISTERED_DATE=models.DateField()
    VEHICLE=models.ForeignKey(to=Driver,on_delete=models.CASCADE)
    ISSUE=models.TextField()
    def __str__(self):
        return self.REGISTERED_DATE