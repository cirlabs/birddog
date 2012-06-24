from django.db import models
from django.template.defaultfilters import slugify

class Agency(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30,blank=True)

    class Meta:
        verbose_name_plural = 'Agencies'

    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Agency, self).save(*args, **kwargs)