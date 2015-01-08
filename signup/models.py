from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=255)

    email = models.EmailField(null=True, blank=True)

    want_to_know = models.TextField(null=True, blank=True)
    can_help_with = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'attendee'
        verbose_name_plural = 'attendees'

    def __str__(self):
        return u'{}'.format(self.name)
