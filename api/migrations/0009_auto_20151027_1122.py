# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_api_sync_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='api',
            name='sync_contacts',
        ),
        migrations.RemoveField(
            model_name='api',
            name='ticket',
        ),
        migrations.AddField(
            model_name='api',
            name='create_ticket',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/create_ticket/', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='api',
            name='get_my_friends',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/get_my_friends/', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='api',
            name='reffered',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/reffered/', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='api',
            name='sync',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/sync/', max_length=100, blank=True),
        ),
    ]
