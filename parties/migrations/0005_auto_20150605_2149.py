# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import icalendar


def create_ical(apps, schema_editor):
    Party = apps.get_model("parties", "Party")
    for party in Party.objects.all():
        event = icalendar.Event()
        event.add('dtstart', party.start)
        if party.end:
            event.add('dtend', party.end)
        event.add('summary', party.title)
        event.add('description', party.description)
        party.ical = event.to_ical()
        party.save()

class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0004_auto_20150605_2320'),
    ]

    operations = [
        migrations.RunPython(
            create_ical,
            migrations.RunPython.noop,
        )
    ]
