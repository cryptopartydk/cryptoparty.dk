from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=255)

    email = models.EmailField(null=True, blank=True)

    want_to_know = models.TextField()
    can_help_with = models.TextField()

    class Meta:
        verbose_name = 'attendee'
        verbose_name_plural = 'attendees'
