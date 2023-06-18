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


class Meet(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    meet_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
