# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_api_my_profile_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='ticket',
        ),
        migrations.AddField(
            model_name='api',
            name='ticket_create',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/ticket_create/', max_length=100, blank=True),
        ),
    ]
