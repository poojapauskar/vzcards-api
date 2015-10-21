# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_api_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='ticket_details',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/ticket_details/', max_length=100, blank=True),
        ),
    ]
