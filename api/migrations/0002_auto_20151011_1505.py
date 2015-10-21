# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='create_object',
        ),
        migrations.AddField(
            model_name='api',
            name='ticket',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/ticket/', max_length=100, blank=True),
        ),
    ]
