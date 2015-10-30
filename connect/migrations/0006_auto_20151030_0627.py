# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0005_auto_20151030_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='ticket_1_dates',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='ticket_2_dates',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
