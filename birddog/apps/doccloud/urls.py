from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^list/$', 'apps.doccloud.views.list', name='docs_list'),
    url(r'^detail/(?P<slug>[\w-]+)/$', 'apps.doccloud.views.detail', name='docs_detail'),
    #url(r'^detail/$', 'apps.doccloud.views.detail', name='docs_detail'),
    url(r'^create/$', 'apps.doccloud.views.create', name='docs_create'),
    url(r'^upload/$', 'apps.doccloud.views.upload', name='docs_upload'),
)