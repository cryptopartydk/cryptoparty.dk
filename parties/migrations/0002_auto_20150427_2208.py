# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='venue',
            field=models.ForeignKey(related_query_name='parties', to='parties.Venue'),
        ),
    ]
