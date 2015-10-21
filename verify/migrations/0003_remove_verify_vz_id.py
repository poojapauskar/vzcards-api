# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0002_auto_20151010_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verify',
            name='vz_id',
        ),
    ]
