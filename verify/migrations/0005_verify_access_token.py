# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0004_auto_20151014_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='verify',
            name='access_token',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
