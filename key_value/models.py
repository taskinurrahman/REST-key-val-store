from django.db import models
import datetime
# Create your models here.
class Store(models.Model):
    key = models.CharField(max_length=1000)
    value = models.CharField(max_length=1000)
    created_at = models.DateTimeField()