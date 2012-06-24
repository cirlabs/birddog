from django.conf.urls.defaults import *

from .views import AgencyListView, AgencyDetailView


urlpatterns = patterns('',
    url(r'detail/(?P<slug>.+)/$', AgencyDetailView.as_view(), name="agency_detail"),
    url(r'list/$', AgencyListView.as_view(), name="agency_list"),
)
