from django.db import models

from clinic.models import ClinicProfile
from patient.models import PatientProfile


class Appointment(models.Model):
    clinic = models.ForeignKey(ClinicProfile,
                               on_delete=models.CASCADE,
                               related_name='appointments')
    patient = models.ForeignKey(PatientProfile,
                                on_delete=models.CASCADE,
                                related_name='appointments')
    _datetime = models.DateTimeField()
    _appointment_duration_in_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f'clinic: {self.clinic.user.username} - ' \
               f'patient: {self.patient.user.username} - ' \
               f'datetime: {self._datetime}'

    def save(self, *args, **kwargs):
        self._datetime = self.clinic.next_available_appointment_datetime
        self._appointment_duration_in_minutes = self.clinic.appointment_duration_in_minutes
        super(Appointment, self).save(*args, **kwargs)

    def get_appointment_duration_in_minutes(self):
        return self._appointment_duration_in_minutes

    def get_datetime(self):
        return self._datetime
