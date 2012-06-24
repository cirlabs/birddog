from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.users.forms import UserRegistrationForm

from registration.views import register
import registration.backends.default.urls as regUrls
import apps.users.regbackend
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    # Simple login for securing site on Heroku
    (r'^/$', 'apps.users.views.register_complete'),#change me
    url(r'^docs/$', 'apps.doccloud.views.index', name='docs_index'),
    url(r'^docs/upload/$', 'apps.doccloud.views.upload', name='docs_upload'),
    # (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),

    # Logging in
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', register,\
        {'backend': 'registration.backends.simple.SimpleBackend',\
        'form_class': UserRegistrationForm, 'success_url': '/'}, name='registration_register'),

    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Project URLs go here

    (r'^requests/', include('apps.requests.urls')),

    url(r'^$', direct_to_template, {'template': 'index.html'}, name='front_page'),
)

urlpatterns += staticfiles_urlpatterns()

