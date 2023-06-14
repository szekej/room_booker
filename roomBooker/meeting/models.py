from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    floor = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
