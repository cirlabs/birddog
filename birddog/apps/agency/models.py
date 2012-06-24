from django.db import models

from django_extensions.db.fields import AutoSlugField


class Agency(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=('name', ))

    class Meta:
        verbose_name_plural = 'Agencies'

    def __unicode__(self):
        return self.name

    @property
    def late_requests(self):
        """
        How many requests have FAILED to meet their deadlines?
        """
        num_late_requests = 0
        for r in self.related_agencies.all():
            if r.is_late_naive: num_late_requests += 1
        return num_late_requests

    @property
    def average_time_outstanding(self):
        days_late = 0
        for r in self.related_agencies.all():
            days_late += r.time_outstanding
        return days_late      
