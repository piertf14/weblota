from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):

    dni = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    is_client = models.BooleanField(
        default=False
    )
    birth_date = models.DateField(
        null=True,
        blank=True
    )
    telephone = models.CharField(
        max_length=11
    )