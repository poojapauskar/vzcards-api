# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_api_my_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='response',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/response/', max_length=100, blank=True),
        ),
    ]
