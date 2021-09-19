from django import forms

from appointment.models import Appointment


class ReserveAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReserveAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['clinic'].disabled = True
        self.fields['patient'].disabled = True
        self.fields['_datetime'].disabled = True
        self.fields['_appointment_duration_in_minutes'].disabled = True

    class Meta:
        model = Appointment
        fields = ['clinic', 'patient', '_datetime', '_appointment_duration_in_minutes']
