# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0002_auto_20150204_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'verbose_name_plural': 'parties', 'verbose_name': 'party'},
        ),
        migrations.AddField(
            model_name='party',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
