from django.urls import path

from appointment import views

urlpatterns = [
    path('reserve/<str:clinic_username>/', views.ReserveAppointment.as_view(), name='reserve-appointment'),
]
