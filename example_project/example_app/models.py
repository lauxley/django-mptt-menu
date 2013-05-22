from django.db import models
from django.core.urlresolvers import reverse


class ExampleModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('example_detail', kwargs={'slug':self.slug})

    def __unicode__(self):
        return unicode(self.title)
