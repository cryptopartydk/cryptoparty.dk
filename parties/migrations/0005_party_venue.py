# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0004_auto_20150427_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='venue',
            field=models.ForeignKey(to='parties.Venue', related_query_name='parties_here', null=True),
        ),
    ]
