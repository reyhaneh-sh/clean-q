from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView

from appointment.models import Appointment
from clinic.decorators import clinic_required
from clinic.forms import ClinicRegisterForm, ClinicProfileUpdateForm
from clinic.models import ClinicProfile as Clinic
from user.forms import UserProfileUpdateForm


class ClinicListView(ListView):
    model = Clinic
    template_name = 'clinic/home_page.html'
    context_object_name = 'clinics'
    paginate_by = 10

    def get_queryset(self):
        name = self.request.GET.get('clinic_name', '')
        queryset = self.model.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset.order_by('specialty')


class ClinicDetailView(DetailView):
    model = Clinic
    template_name = 'clinic/clinic_detail.html'
    context_object_name = 'clinic'

    def get_slug_field(self):
        return 'user__username'


class ClinicRegister(APIView):
    @staticmethod
    def get(request):
        form = ClinicRegisterForm()
        return render(request, 'clinic/register.html', {'form': form})

    @staticmethod
    def post(request):
        form = ClinicRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You are now able to login.')
            return redirect('login')
        return render(request, 'clinic/register.html', {'form': form})


class ClinicProfile(APIView):
    @staticmethod
    @login_required
    @clinic_required
    def get(request):
        user_profile_form = UserProfileUpdateForm(instance=request.user)
        clinic_profile_form = ClinicProfileUpdateForm(
            instance=request.user.clinicprofile)

        context = {
            'user_profile_form': user_profile_form,
            'clinic_profile_form': clinic_profile_form
        }

        return render(request, 'clinic/profile.html', context)

    @staticmethod
    @login_required
    @clinic_required
    def post(request):
        user_profile_form = UserProfileUpdateForm(request.POST,
                                                  instance=request.user)
        clinic_profile_form = ClinicProfileUpdateForm(request.POST,
                                                      instance=request.user.clinicprofile)
        if user_profile_form.is_valid() and clinic_profile_form.is_valid():
            user_profile_form.save()
            clinic_profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('clinic-profile')


class ClinicAppointments(APIView):
    @staticmethod
    @login_required
    @clinic_required
    def get(request):
        clinic = Clinic.objects.get(user__username=request.user.username)
        appointments = Appointment.objects.filter(clinic=clinic).order_by('_datetime')
        context = {
            'appointments': appointments
        }
        return render(request, 'clinic/appointments.html', context)
