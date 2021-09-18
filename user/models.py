from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_clinic = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = None
    last_name = None
