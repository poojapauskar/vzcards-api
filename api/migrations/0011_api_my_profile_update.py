# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20151027_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='my_profile_update',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/my_profile/update/', max_length=100, blank=True),
        ),
    ]
