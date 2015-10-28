# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0006_auto_20151027_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='verify',
            name='vz_id',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
