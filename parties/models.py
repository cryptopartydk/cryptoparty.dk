from django.core.urlresolvers import reverse
from django.db import models

from django_extensions.db.fields import AutoSlugField
from parties.managers import PartyQuerySet


class Party(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)

    slug = AutoSlugField(populate_from='title')

    description = models.TextField()

    when = models.DateTimeField(help_text='YYYY-MM-DD HH:MM:SS')

    venue = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)

    public = models.BooleanField(default=False)

    organizers = models.ManyToManyField(
        'auth.User',
        blank=True,
        related_name='parties'
    )

    objects = PartyQuerySet.as_manager()

    class Meta:
        verbose_name = 'party'
        verbose_name_plural = 'parties'

    def __str__(self):
        return '"{}" at {}'.format(self.title, self.venue)

    def get_absolute_url(self):
        return reverse('parties:party-detail', kwargs={'slug': self.slug})
