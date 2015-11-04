# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0006_auto_20151030_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connect',
            name='connecter_details',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='phone_1_details',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='phone_2_details',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ticket_1_dates',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ticket_1_details',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ticket_2_dates',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ticket_2_details',
        ),
    ]
