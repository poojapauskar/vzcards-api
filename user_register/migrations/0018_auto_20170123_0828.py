# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0017_auto_20170120_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='is_organization',
            field=models.CharField(default=b'true', max_length=100, blank=True),
        ),
    ]
