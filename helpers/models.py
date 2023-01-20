from django.db import models

class Tracking(models.Model):
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateField(auto_now=True)
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status=models.CharField(max_length=50, choices=STATUS,default='Active')

    class Meta:
        abstract = True
        ordering = ('-created_at',)