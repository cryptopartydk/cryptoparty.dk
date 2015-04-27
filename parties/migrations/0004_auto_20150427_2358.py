# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0003_remove_party_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='venue',
        ),
        migrations.AlterField(
            model_name='party',
            name='organizers',
            field=models.ManyToManyField(blank=True, related_name='organizing_parties', to=settings.AUTH_USER_MODEL),
        ),
    ]
