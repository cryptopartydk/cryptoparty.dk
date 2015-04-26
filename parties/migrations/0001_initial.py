# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from='title', blank=True)),
                ('description', models.TextField()),
                ('when', models.DateTimeField(help_text='YYYY-MM-DD HH:MM:SS')),
                ('venue', models.CharField(max_length=100)),
                ('address', models.CharField(null=True, max_length=100, blank=True)),
                ('city', models.CharField(null=True, max_length=100, blank=True)),
                ('postal_code', models.IntegerField(null=True, blank=True)),
                ('public', models.BooleanField(default=False)),
                ('organizers', models.ManyToManyField(related_name='parties', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': 'party',
                'verbose_name_plural': 'parties',
            },
        ),
    ]
