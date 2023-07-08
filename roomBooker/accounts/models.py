from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    objects = UserManager()
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_set'
    )

    def __str__(self):
        return self.username
