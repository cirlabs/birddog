from django.db import models

class Agency(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name_plural = 'Agencies'

    def __unicode__(self):
        return self.name