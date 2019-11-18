from django.db import models


# Create your models here.

class Message(models.Model):
    key = models.CharField(max_length=256)
    message = models.CharField(max_length=256)
