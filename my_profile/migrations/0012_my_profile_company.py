# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0011_auto_20151016_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_profile',
            name='company',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
