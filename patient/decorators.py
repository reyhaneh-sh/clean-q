from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from clean_q.settings import LOGIN_URL


def patient_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    actual_decorator = user_passes_test(
        lambda user: user.is_patient,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
