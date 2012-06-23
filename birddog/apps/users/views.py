from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import UserProfile, Organization
from django.template.defaultfilters import slugify


def register_complete(request, template_name='registration/registration_complete.html'):
    context = {}   
    return render_to_response(template_name, context, context_instance=RequestContext(request))