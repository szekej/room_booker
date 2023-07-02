from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django import forms
from django.forms.widgets import TimeInput


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    floor = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Meet(models.Model, forms.TimeField):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    meet_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def clean(self):    # override default method to validate model
        super().clean()
        if self.start_time and self.end_time:
            if self.end_time <= self.start_time:
                raise ValidationError("End time cannot be set before the start time")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
