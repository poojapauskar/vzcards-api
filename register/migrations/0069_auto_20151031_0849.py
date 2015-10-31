# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0068_auto_20151031_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='photo',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
