from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request


class NewRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('title', 'agency')


class NewOptionalRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('text', 'tags', 'private', 'document')
