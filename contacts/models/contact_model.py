from django.db import models
from django.utils import timezone


class Contact(models.Model):
    phone_number = models.CharField(max_length=15, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    updated_at = models.DateTimeField(auto_now=timezone.now())
