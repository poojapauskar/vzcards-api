# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0007_remove_my_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_profile',
            name='vz_id',
        ),
    ]
