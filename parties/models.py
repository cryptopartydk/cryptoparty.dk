from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField, UUIDField
from parties.managers import PartyQuerySet


class Party(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    title = models.CharField(max_length=100)

    slug = AutoSlugField(populate_from='title')

    description = models.TextField()

    when = models.DateTimeField(help_text='YYYY-MM-DD HH:MM:SS')

    venue = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)

    public = models.BooleanField(default=False)

    creator_email = models.EmailField(null=True, blank=True)

    key = UUIDField()

    objects = PartyQuerySet.as_manager()

    class Meta:
        verbose_name = 'party'
        verbose_name_plural = 'parties'

    def __str__(self):
        return '"{}" at {}'.format(self.title, self.venue)


class Attendee(models.Model):
    party = models.ForeignKey('parties.Party')
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    CRYPTO_LEVELS = [
        ('knows', _('Knows crypto')),
        ('newbie', _('Does not know crypto')),
    ]

    crypto_level = models.CharField(choices=CRYPTO_LEVELS, max_length=20)

    class Meta:
        verbose_name = 'attendee'
        verbose_name_plural = 'attendees'

    def __unicode__(self):
        return u'{}'.format(self.name)
