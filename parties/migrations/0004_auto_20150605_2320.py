# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0003_party_venue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ['start'], 'verbose_name': 'party', 'verbose_name_plural': 'parties'},
        ),
        migrations.RenameField(
            model_name='party',
            old_name='when',
            new_name='start',
        ),
        migrations.AddField(
            model_name='party',
            name='end',
            field=models.DateTimeField(blank=True, null=True, help_text='YYYY-MM-DD HH:MM:SS'),
        ),
        migrations.AddField(
            model_name='party',
            name='ical',
            field=models.TextField(blank=True, null=True),
        ),
    ]
