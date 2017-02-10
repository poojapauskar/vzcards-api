# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_auto_20151015_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_profile',
            name='vz_id',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
