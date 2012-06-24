from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    organization = models.ForeignKey('Organization')
    private_by_default = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username


class Organization(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)
    logo = models.ImageField(upload_to='logos', blank=True, null=True, max_length=255)

    def __unicode__(self):
        return self.name