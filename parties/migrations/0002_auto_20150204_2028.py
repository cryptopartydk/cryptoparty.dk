# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='venue_name',
            new_name='venue',
        ),
    ]
