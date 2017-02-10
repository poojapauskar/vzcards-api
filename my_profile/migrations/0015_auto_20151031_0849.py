# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0014_my_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_profile',
            name='photo',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
