# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0003_auto_20150208_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='creator_email',
            field=models.EmailField(null=True, max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
