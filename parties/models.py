from django.db import models

from django_extensions.db.fields import AutoSlugField, UUIDField


class Party(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    title = models.CharField(max_length=100)

    slug = AutoSlugField(populate_from='title')

    description = models.TextField()

    when = models.DateTimeField(help_text='YYYY-MM-DD HH:MM:SS')

    venue_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)

    key = UUIDField()

    def __str__(self):
        return '"{}" at {}'.format(self.title, self.venue_name)


class Attendee(models.Model):
    party = models.ForeignKey('parties.Party')
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    CRYPTO_LEVELS = [
        ('knows', 'Knows crypto'),
        ('newbie', 'Does not know crypto')
    ]

    crypto_level = models.CharField(choices=CRYPTO_LEVELS, max_length=20)

    class Meta:
        verbose_name = 'attendee'
        verbose_name_plural = 'attendees'

    def __unicode__(self):
        return u'{}'.format(self.name)
