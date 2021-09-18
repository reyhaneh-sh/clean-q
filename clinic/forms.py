from django import forms
from django.contrib.auth.forms import UserCreationForm

from clinic.constants.specialty_title import SpecialtyTitle
from clinic.models import ClinicProfile
from user.models import User


class ClinicRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    specialty = forms.ChoiceField(choices=SpecialtyTitle.CHOICES)
    address = forms.CharField(max_length=300)
    phone_number = forms.CharField(max_length=11)
    description = forms.CharField(max_length=700,
                                  required=False)
    first_name = None
    last_name = None

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_clinic = True
        user.save()
        clinic = ClinicProfile.objects.create(user=user)
        clinic.name = self.cleaned_data.get('name')
        clinic.specialty = self.cleaned_data.get('specialty')
        clinic.address = self.cleaned_data.get('address')
        clinic.phone_number = self.cleaned_data.get('phone_number')
        clinic.description = self.cleaned_data.get('description')
        clinic.save()
        return clinic
