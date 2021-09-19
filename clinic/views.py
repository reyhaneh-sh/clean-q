from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from clinic.decorators import clinic_required
from clinic.forms import ClinicRegisterForm, ClinicProfileUpdateForm
from clinic.models import ClinicProfile as Clinic
from user.forms import UserProfileUpdateForm


def home(request):
    context = {
        'clinics': Clinic.objects.all()
    }
    return render(request, 'clinic/home_page.html', context)


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
