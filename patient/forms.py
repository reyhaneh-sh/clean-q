from django import forms
from django.contrib.auth.forms import UserCreationForm

from patient.constants.birth_date import BirthDate
from patient.constants.sex_status import SexStatus
from patient.models import PatientProfile
from user.models import User


class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    mobile_number = forms.CharField(max_length=11)
    sex = forms.ChoiceField(choices=SexStatus.CHOICES)
    birth_date = forms.DateField(required=False,
                                 widget=forms.SelectDateWidget(years=BirthDate.YEARS))

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = PatientProfile.objects.create(user=user)
        patient.first_name = self.cleaned_data.get('first_name')
        patient.last_name = self.cleaned_data.get('last_name')
        patient.mobile_number = self.cleaned_data.get('mobile_number')
        patient.sex = self.cleaned_data.get('sex')
        patient.birth_date = self.cleaned_data.get('birth_date')
        patient.save()
        return patient
