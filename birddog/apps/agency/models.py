from django.db import models

from django_extensions.db.fields import AutoSlugField


class Agency(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=('name', ))

    class Meta:
        verbose_name_plural = 'Agencies'

    def __unicode__(self):
        return self.name
