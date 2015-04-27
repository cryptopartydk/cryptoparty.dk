# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
from django.conf import settings


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
                ('address', models.CharField(max_length=100, blank=True, null=True)),
                ('public', models.BooleanField(default=False)),
                ('organizers', models.ManyToManyField(related_name='parties', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'parties',
                'verbose_name': 'party',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255, blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='party',
            name='venue',
            field=models.ForeignKey(to='parties.Venue'),
        ),
    ]
