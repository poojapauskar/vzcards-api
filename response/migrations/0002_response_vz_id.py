# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='vz_id',
            field=models.CharField(default=b'', max_length=15, blank=True),
        ),
    ]
