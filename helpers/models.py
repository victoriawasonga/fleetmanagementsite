from django.db import models

class Tracking(models.Model):
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateField(auto_now=True)
    STATUS = (
        ('A', 'Active'),
        ('N', 'Not Active'),
    )
    STATUS=models.CharField(max_length=1, choices=STATUS)

    class Meta:
        abstract = True
        ordering = ('-created_at',)