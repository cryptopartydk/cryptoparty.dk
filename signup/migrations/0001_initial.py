# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(null=True, blank=True, max_length=75)),
                ('want_to_know', models.TextField()),
                ('can_help_with', models.TextField()),
            ],
            options={
                'verbose_name': 'attendee',
                'verbose_name_plural': 'attendees',
            },
            bases=(models.Model,),
        ),
    ]
