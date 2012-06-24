from django import forms

from apps.agency.models import Agency
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request


class NewRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('title', 'agency', 'private')
        widgets = {
                'private': forms.widgets.CheckboxInput
            }

    agency = forms.ModelChoiceField(
                queryset=Agency.objects.all(),
                widget=forms.widgets.SelectMultiple,
                empty_label=None
            )


class NewOptionalRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('text', 'tags', 'document')
