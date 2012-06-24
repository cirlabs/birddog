import datetime
from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager

from apps.doccloud.models import Document
from apps.agency.models import Agency


class Request(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=(('P', 'Pending'), ('F', 'Filled')))
    agencies = models.ManyToManyField(Agency, blank=True, null=True, related_name='related_agencies')
    documents = models.ManyToManyField(Document, blank=True, null=True, related_name='related_docs')
    text = models.TextField(u'Request text', blank=True)
    private = models.BooleanField('Mark this request as private', default=False)
    supporters = models.ManyToManyField(User, blank=True, null=True, related_name='supporter')
    slug = AutoSlugField(populate_from=('title', ), overwrite=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_fulfilled = models.DateTimeField(blank=True, null=True)

    # Managers
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    @property
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
        try: # AHHHH HACK CITY!!!
            e = self.event_set.filter(type=2).order_by('date')[0]
        except IndexError:
            return
        return e.date

    @property
    def latest_deadline(self):
        try: # AHHHH HACK CITY!!!
            e = self.event_set.filter(type=2).order_by('date')[0]
        except IndexError:
            return
        return e.date

    @property
    def is_late_naive(self):
        """
        Naive representation of whether a response is late. Will
        want to redo this with more 
        """
        is_late = False
        if self.latest_deadline: # AHHHH HACK CITY!!!
            if datetime.date.today() > self.latest_deadline:
                is_late = True
        return is_late


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
