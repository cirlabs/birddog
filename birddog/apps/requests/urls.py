from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from .views import RequestListView, RequestDetailView, new_request


urlpatterns = patterns('',
    url(r'new/$', new_request, name="request_new"),
    url(r'list/$', login_required(RequestListView.as_view()), name="request_list"),
    url(r'detail/(?P<slug>.+)/edit/$', login_required(RequestDetailView.as_view()), name="request_edit"),
    url(r'detail/(?P<slug>.+)/$', RequestDetailView.as_view(), name="request_detail"),
)