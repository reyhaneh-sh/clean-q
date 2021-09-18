import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from clinic.constants.specialty_title import SpecialtyTitle
from user.models import User


class ClinicProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50,
                                 choices=SpecialtyTitle.CHOICES)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=11)
    opening_time = models.TimeField(default=datetime.time(8, 0))
    closing_time = models.TimeField(default=datetime.time(21, 0))
    appointment_duration_in_minutes = models.PositiveIntegerField(default=30)
    description = models.CharField(max_length=700,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return f'username: {self.user.username} - name: {self.name}'
