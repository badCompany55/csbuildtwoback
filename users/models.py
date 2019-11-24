from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class CustomUser(AbstractUser):
    backtoken = models.TextField(blank=False)


class Status(models.Model):
    player = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    inventory = JSONField(default=dict)
    current_room = models.IntegerField()

