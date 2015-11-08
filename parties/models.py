from django.core.urlresolvers import reverse
from django.db import models

from django_extensions.db.fields import AutoSlugField
import icalendar
from parties.managers import PartyQuerySet


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Party(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(
        max_length=100,
    )

    slug = AutoSlugField(
        populate_from='title',
    )

    description = models.TextField()

    start = models.DateTimeField(
        help_text='YYYY-MM-DD HH:MM:SS',
    )

    end = models.DateTimeField(
        help_text='YYYY-MM-DD HH:MM:SS',
        null=True,
        blank=True,
    )

    venue = models.ForeignKey(
        Venue,
        related_query_name="parties_here",
        null=True,
    )

    public = models.BooleanField(
        default=False,
    )

    organizers = models.ManyToManyField(
        'auth.User',
        blank=True,
        related_name='organizing_parties',
    )

    ical = models.TextField(null=True, blank=True)

    objects = PartyQuerySet.as_manager()

    class Meta:
        verbose_name = 'party'
        verbose_name_plural = 'parties'
        ordering = ['start']

    def __str__(self):
        return '"{}" at {}'.format(self.title, self.venue)

    def get_absolute_url(self):
        return reverse('parties:party-detail', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        if not self.slug:
            super().save(**kwargs)
        event = icalendar.Event()
        event.add('dtstart', self.start)
        if self.end:
            event.add('dtend', self.end)
        event.add('summary', self.title)
        event.add(
            'description',
            '{}\n\n{}'.format(
                self.get_absolute_url(),
                self.description
            )
        )
        self.ical = event.to_ical()
        super().save(**kwargs)
