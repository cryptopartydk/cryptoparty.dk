# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0002_auto_20150428_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='venue',
            field=models.ForeignKey(related_query_name='parties_here', to='parties.Venue', null=True),
        ),
    ]
