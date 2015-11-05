# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_api_upload_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='history',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/history/', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='api',
            name='remove_ticket',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/remove_ticket/', max_length=100, blank=True),
        ),
    ]
