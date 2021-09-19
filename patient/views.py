from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from patient.forms import PatientSignUpForm, PatientProfileUpdateForm
from user.forms import UserProfileUpdateForm


class PatientSignUp(APIView):
    @staticmethod
    def get(request):
        form = PatientSignUpForm()
        return render(request, 'patient/signup.html', {'form': form})

    @staticmethod
    def post(request):
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You are now able to login.')
            return redirect('login')
        return render(request, 'patient/signup.html', {'form': form})


class PatientProfile(APIView):
    @staticmethod
    @login_required
    def get(request):
        user_profile_form = UserProfileUpdateForm(instance=request.user)
        patient_profile_form = PatientProfileUpdateForm(
            instance=request.user.patientprofile)

        context = {
            'user_profile_form': user_profile_form,
            'patient_profile_form': patient_profile_form
        }

        return render(request, 'patient/profile.html', context)

    @staticmethod
    @login_required
    def post(request):
        user_profile_form = UserProfileUpdateForm(request.POST,
                                                  instance=request.user)
        patient_profile_form = PatientProfileUpdateForm(request.POST,
                                                        instance=request.user.patientprofile)
        if user_profile_form.is_valid() and patient_profile_form.is_valid():
            user_profile_form.save()
            patient_profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('patient-profile')
