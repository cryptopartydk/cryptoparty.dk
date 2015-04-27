# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0003_remove_party_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='organizers',
            field=models.ManyToManyField(related_name='organizing_parties', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='party',
            name='venue',
            field=models.ForeignKey(related_query_name='parties_here', to='parties.Venue'),
        ),
    ]
