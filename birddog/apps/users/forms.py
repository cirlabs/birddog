from django import forms
from apps.users.models import Organization
from registration.forms import RegistrationForm


class UserRegistrationForm(RegistrationForm):
    organization = forms.CharField(max_length=255)