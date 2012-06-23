from django.conf.urls.defaults import *
from apps.requests.views import RequestListView, RequestDetailView

urlpatterns = patterns('',
    url(r'list/$', RequestListView.as_view(), name="request_list"),
    url(r'detail/(?P<slug>.+)/$', RequestDetailView.as_view(), name="request_detail"),
)
