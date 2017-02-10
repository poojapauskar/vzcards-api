# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0009_auto_20151016_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_profile',
            name='your_vz_id',
        ),
        migrations.AddField(
            model_name='my_profile',
            name='vz_id',
            field=models.CharField(default=b'', max_length=15, editable=False, blank=True),
        ),
    ]
