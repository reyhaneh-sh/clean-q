from django.shortcuts import render

from clinic.models import ClinicProfile


def home(request):
    context = {
        'clinics': ClinicProfile.objects.all()
    }
    return render(request, 'clinic/home_page.html', context)
