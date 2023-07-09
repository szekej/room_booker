from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import CustomUser


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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

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
