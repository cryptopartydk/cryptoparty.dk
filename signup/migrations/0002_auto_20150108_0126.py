# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='can_help_with',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='want_to_know',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
