from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import UserProfile, Organization
from apps.users.forms import OrganizationForm
from django.template.defaultfilters import slugify

def register(request, template_name='registration/registration_form.html'):
    context = {}
    if request.method == 'GET':
        create_form = UserCreationForm()
        org_form = OrganizationForm()
        context['form'] = create_form
        context['org_form'] = org_form
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        org_form = OrganizationForm(request.POST)
        if form.is_valid() and org_form.is_valid(): 
            name = org_form.cleaned_data['name']
            org_slug = slugify(name)
            user_org, created = Organization.objects.get_or_create(name=name, slug=org_slug)
            user_org.save()

            new_user = form.save()
            userprofile, created = UserProfile.objects.get_or_create(user=new_user, organization=user_org)
            print 'yay'
            return HttpResponseRedirect('/registration/registration_complete.html')
        else:
            print 'boo'
            import pdb;pdb.set_trace()

    return render_to_response(template_name, context, context_instance=RequestContext(request))