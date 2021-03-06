from django import forms

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


class NewOptionalRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('text', 'tags', 'documents')
