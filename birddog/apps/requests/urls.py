from django.conf.urls.defaults import *
from apps.requests.views import RequestListView, RequestDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'list/$', RequestListView.as_view(), name="request_list"),
    url(r'detail/(?P<slug>.+)/edit/$', login_required(RequestDetailView.as_view()), name="request_edit"),
    url(r'detail/(?P<slug>.+)/$', RequestDetailView.as_view(), name="request_detail"),
    
    
)
