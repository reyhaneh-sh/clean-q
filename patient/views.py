from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from patient.forms import PatientSignUpForm


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
