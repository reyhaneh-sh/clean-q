from django.urls import path

from patient import views

urlpatterns = [
    path('signup/', views.PatientSignUp.as_view(), name='patient-signup'),
]
