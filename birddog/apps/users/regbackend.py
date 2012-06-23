from apps.users.models import UserProfile, Organization
from apps.users.forms import UserRegistrationForm
from django.template.defaultfilters import slugify


def user_created(sender, user, request, **kwargs):
    form = UserRegistrationForm(request.POST)
    name = form.data['organization']
    org_slug = slugify(name)
    user_org, created = Organization.objects.get_or_create(name=name, slug=org_slug)
    userprofile, created = UserProfile.objects.get_or_create(user=user, organization=user_org)

from registration.signals import user_registered
user_registered.connect(user_created)