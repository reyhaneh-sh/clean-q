import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from clinic.constants.specialty_title import SpecialtyTitle
from user.models import User, Profile


class ClinicProfile(Profile):
    @property
    def next_available_appointment_datetime(self):
        appointments = self.appointments.filter().order_by('-_datetime')
        if len(appointments) > 0:
            latest_appointment = appointments[0]
            today_next_appointment_datetime = self._get_today_next_appointment_datetime(latest_appointment)
            if self._today_next_appointment_datetime_is_valid(today_next_appointment_datetime):
                return today_next_appointment_datetime
            return self._get_tomorrow_first_appointment_datetime()
        return self._get_today_first_appointment_datetime()

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

    @staticmethod
    def _get_today_next_appointment_datetime(latest_appointment):
        latest_appointment_duration = latest_appointment.get_appointment_duration_in_minutes()
        return latest_appointment._datetime + datetime.timedelta(minutes=latest_appointment_duration)

    def _today_next_appointment_datetime_is_valid(self, today_next_appointment_datetime):
        appointment_duration = datetime.timedelta(minutes=self.appointment_duration_in_minutes)
        appointment_end_datetime = today_next_appointment_datetime + appointment_duration
        if appointment_end_datetime.time() <= self.closing_time:
            return True
        return False

    def _get_tomorrow_first_appointment_datetime(self):
        tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)
        return datetime.datetime.combine(tomorrow_date, self.opening_time)

    def _get_today_first_appointment_datetime(self):
        return datetime.datetime.combine(datetime.date.today(), self.opening_time)
