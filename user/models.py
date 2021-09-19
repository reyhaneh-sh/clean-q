from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_clinic = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = None
    last_name = None


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username
