from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from clinic.forms import ClinicRegisterForm
from clinic.models import ClinicProfile


def home(request):
    context = {
        'clinics': ClinicProfile.objects.all()
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
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('clean-q-home')
        return render(request, 'clinic/register.html', {'form': form})
