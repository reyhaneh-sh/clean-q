from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from appointment.forms import ReserveAppointmentForm
from clinic.models import ClinicProfile
from patient.decorators import patient_required
from patient.models import PatientProfile


class ReserveAppointment(APIView):
    @staticmethod
    @login_required
    @patient_required
    def get(request, clinic_username):
        clinic = ClinicProfile.objects.get(user__username=clinic_username)
        patient = PatientProfile.objects.get(user__username=request.user.username)
        form = ReserveAppointmentForm(initial={'clinic': clinic,
                                               'patient': patient,
                                               '_datetime': clinic.next_available_appointment_datetime,
                                               '_appointment_duration_in_minutes': clinic.appointment_duration_in_minutes})
        return render(request, 'appointment/appointment_form.html', {'form': form})

    @staticmethod
    @login_required
    @patient_required
    def post(request, clinic_username):
        clinic = ClinicProfile.objects.get(user__username=clinic_username)
        patient = PatientProfile.objects.get(user__username=request.user.username)
        form = ReserveAppointmentForm(request.POST, initial={'clinic': clinic,
                                                             'patient': patient,
                                                             '_datetime': clinic.next_available_appointment_datetime,
                                                             '_appointment_duration_in_minutes': clinic.appointment_duration_in_minutes})
        if form.is_valid():
            form.save()
            messages.success(request, f'Your appointment has been reserved.')
            return redirect('clean-q-home')
        return render(request, 'appointment/appointment_form.html', {'form': form})
