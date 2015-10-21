# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_api_send_again'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='my_profile',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/my_profile/', max_length=100, blank=True),
        ),
    ]
