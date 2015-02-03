# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('crypto_level', models.CharField(max_length=20, choices=[('knows', 'Knows crypto'), ('newbie', 'Does not know crypto')])),
            ],
            options={
                'verbose_name_plural': 'attendees',
                'verbose_name': 'attendee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='title', blank=True, editable=False)),
                ('description', models.TextField()),
                ('when', models.DateTimeField(help_text='YYYY-MM-DD HH:MM:SS')),
                ('venue_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('postal_code', models.IntegerField(null=True, blank=True)),
                ('key', django_extensions.db.fields.UUIDField(blank=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attendee',
            name='party',
            field=models.ForeignKey(to='parties.Party'),
            preserve_default=True,
        ),
    ]
