# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20151027_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='create_ticket',
        ),
        migrations.AddField(
            model_name='api',
            name='ticket',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/ticket/', max_length=100, blank=True),
        ),
    ]
