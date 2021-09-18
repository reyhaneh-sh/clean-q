from django.urls import path

from clinic import views

urlpatterns = [
    path('register/', views.ClinicRegister.as_view(), name='clinic-register'),
]