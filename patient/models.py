from django.db import models

from patient.constants.sex_status import SexStatus
from user.models import User, Profile


class PatientProfile(Profile):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=11)
    sex = models.CharField(max_length=30,
                           choices=SexStatus.CHOICES,
                           default=SexStatus.DEFAULT)
    birth_date = models.DateField(null=True,
                                  blank=True,
                                  auto_now=False,
                                  auto_now_add=False)

    def __str__(self):
        return f'username: {self.user.username}' \
               f' - full name: {self.first_name} {self.last_name}'
