from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    organization = models.ForeignKey('Organization')
    private_by_default = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)

    def __unicode__(self):
        return self.name