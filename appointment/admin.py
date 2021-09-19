from django.contrib import admin

from appointment.models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ['_appointment_duration_in_minutes', '_datetime']


admin.site.register(Appointment, AppointmentAdmin)
