# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0010_auto_20151016_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_profile',
            name='vz_id',
            field=models.CharField(default=b'', max_length=15, blank=True),
        ),
    ]
