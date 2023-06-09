from django.db import models
from django.utils import timezone


# Create your models here.

class Device(models.Model):
    serial_number = models.AutoField(unique=True, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
