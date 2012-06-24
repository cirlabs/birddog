from django import forms

from apps.agency.models import Agency
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request


class NewRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('title', 'agencies', 'private')
        widgets = {
                'private': forms.widgets.CheckboxInput
            }

    agencies = forms.ModelMultipleChoiceField(
                queryset=Agency.objects.all(),
                widget=forms.widgets.SelectMultiple,
            )


class NewOptionalRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('text', 'tags', 'documents')
