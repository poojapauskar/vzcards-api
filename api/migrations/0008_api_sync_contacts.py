# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_api_ticket_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='sync_contacts',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/sync_contacts/', max_length=100, blank=True),
        ),
    ]
