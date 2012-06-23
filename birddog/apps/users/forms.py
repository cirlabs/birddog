from django import forms
from apps.users.models import Organization


class OrganizationForm(forms.Form):
    name = forms.CharField(max_length=255)