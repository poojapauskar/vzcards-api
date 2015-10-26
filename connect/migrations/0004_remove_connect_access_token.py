# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_connect_access_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connect',
            name='access_token',
        ),
    ]
