from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.users.forms import UserRegistrationForm

from registration.views import register
import registration.backends.default.urls as regUrls
import apps.users.regbackend

admin.autodiscover()

urlpatterns = patterns('',
    # Simple login for securing site on Heroku
    (r'^/$', 'apps.users.views.register_complete'),#change me
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),

    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', register,\
        {'backend': 'registration.backends.simple.SimpleBackend',\
        'form_class': UserRegistrationForm, 'success_url': '/'}, name='registration_register'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    # Project URLs go here
    (r'^requests/', include('apps.requests.urls')),
)

urlpatterns += staticfiles_urlpatterns()
