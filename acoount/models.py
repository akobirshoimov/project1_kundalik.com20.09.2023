from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (3,'director'),
        (2,'teacher'),
        (1,'student')
    )

    roles = models.PositiveIntegerField(choices=CHOICE_ROLES,default=1)

    def __str__(self) -> str:
        return self.username 