# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151011_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='friends',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/friends/', max_length=100, blank=True),
        ),
    ]
