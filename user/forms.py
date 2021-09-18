from django import forms

from user.models import User


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
