from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property

from django_extensions.db.fields import AutoSlugField
import re
from parties.managers import PartyQuerySet


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Party(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)

    slug = AutoSlugField(populate_from='title')

    description = models.TextField()

    when = models.DateTimeField(help_text='YYYY-MM-DD HH:MM:SS')

    venue = models.ForeignKey(
        Venue,
        related_query_name="parties_here",
        null=True
    )

    public = models.BooleanField(default=False)

    organizers = models.ManyToManyField(
        'auth.User',
        blank=True,
        related_name='organizing_parties'
    )

    objects = PartyQuerySet.as_manager()

    class Meta:
        verbose_name = 'party'
        verbose_name_plural = 'parties'

    def __str__(self):
        return '"{}" at {}'.format(self.title, self.venue)

    def get_absolute_url(self):
        return reverse('parties:party-detail', kwargs={'slug': self.slug})
