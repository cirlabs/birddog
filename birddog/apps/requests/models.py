from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from apps.doccloud.models import Document


class Request(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=(('P', 'Pending'), ('F', 'Filled')))
    agency = models.ForeignKey('Agency', blank=True, null=True)
    document = models.ForeignKey(Document, blank=True, null=True)
    text = models.TextField(u'Request text', blank=True)
    private = models.BooleanField(default=False)
    supporters = models.ManyToManyField(User, blank=True, null=True, related_name='supporter')
    slug = models.SlugField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Managers
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('request_detail', (), {'slug': self.slug})

class Event(models.Model):
    request = models.ForeignKey(Request)
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    # Supporting docs

    def __unicode__(self):
        return '%s -> %s' % (self.request.title, self.name)


class Agency(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name_plural = 'Agencies'

    def __unicode__(self):
        return self.name