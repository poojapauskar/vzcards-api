# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_remove_connect_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='connecter_details',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='phone_1_details',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='phone_2_details',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='ticket_1_details',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='ticket_2_details',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
