from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from apps.doccloud.forms import DocCloudDocForm
from apps.doccloud.models import DocumentCloudProperties
from django.contrib.auth.decorators import login_required

@login_required
def index(request, template_name='doccloud/upload.html'):
    context = {}
    context['form'] = DocCloudDocForm()
    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
def upload(request, template_name='doccloud/complete.html'):
    context = {}
    try:
        if request.method == 'POST':
            dc_form = DocCloudDocForm(request.POST, request.FILES)
            dc_form.user = request.user
            if dc_form.is_valid():
                model = dc_form.save(commit=False)
                model.user = request.user
                model.connect_dc_doc()
                model.save()
            else:
                context['form'] = dc_form
                return render_to_response('doccloud/upload.html', context, context_instance=RequestContext(request))
        else:
            return render_to_response('doccloud/upload.html', context, context_instance=RequestContext(request))
    except Exception as e:
        print e#need logger
    return render_to_response(template_name, context, context_instance=RequestContext(request))