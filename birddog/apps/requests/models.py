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
    date_fulfilled = models.DateTimeField(null=True)
    # Managers
    tags = TaggableManager()
    
    # date_fulfiled?
    
    def __unicode__(self):
        return self.title
    
    def time_outstanding(self):
        from datetime import datetime
        date_filed = self.date_added
        if self.date_fulfilled:
            final_date = self.date_fulfilled
        else:
            final_date = datetime.now()
        date_diff = final_date - date_filed
        return date_diff.days
    
    def original_deadline(self):
        e = self.event_set.filter(type=2).order_by('date')[0]
        return e.date
    
    def latest_deadline(self):
        e = self.event_set.filter(type=2).order_by('date')[0]
        return e.date
    
    @models.permalink
    def get_absolute_url(self):
        return ('request_detail', (), {'slug': self.slug})

class Event(models.Model):
    EVENT_CHOICES = (
        (0, 'Note'),
        (1, 'Reminder'),
        (2, 'Deadline'),
        (3, 'Response')
    )
    request = models.ForeignKey(Request)
    type = models.IntegerField(choices=EVENT_CHOICES)
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