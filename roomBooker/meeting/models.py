from django.db import models
from django.utils.text import slugify


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    floor = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
