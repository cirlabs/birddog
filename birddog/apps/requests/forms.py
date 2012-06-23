from django.forms import ModelForm
from apps.requests.models import Request


class RequestForm(ModelForm):
    class Meta:
        model = Request