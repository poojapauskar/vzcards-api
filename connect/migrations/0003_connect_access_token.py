# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_auto_20151014_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='access_token',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
