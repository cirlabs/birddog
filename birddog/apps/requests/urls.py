from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .models import Request
from .views import RequestListView, RequestDetailView
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'new/$', CreateView.as_view(model=Request, template_name="requests/new.html"), name="request_new"),
    url(r'list/$', login_required(RequestListView.as_view()), name="request_list"),
    url(r'detail/(?P<slug>.+)/edit/$', login_required(RequestDetailView.as_view()), name="request_edit"),
    url(r'detail/(?P<slug>.+)/$', RequestDetailView.as_view(), name="request_detail"),
    
    #agency
    #url(r'detail/(?P<slug>.+)/$', AgencyDetailView.as_view(), name="agency_detail"),
    url(r'detail/$', direct_to_template, {'template': 'requests/agency.html'}, name="agency_detail"),
)