from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .models import Agency
from .views import AgencyListView, AgencyDetailView
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    
    #url(r'detail/(?P<slug>.+)/$', AgencyDetailView.as_view(), name="agency_detail"),
    #url(r'list/$', AgencyListView.as_view(), name="agency_list"),

    url(r'detail/$', direct_to_template, {'template': 'agencies/agency.html'}, name="agency_detail"),
    url(r'list/$', direct_to_template, {'template': 'agencies/agency_list.html'}, name="agency_list"),
)
