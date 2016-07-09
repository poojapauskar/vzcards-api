# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0017_auto_20151128_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_profile',
            name='title',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
