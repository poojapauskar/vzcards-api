# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0052_auto_20151030_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='photo',
        ),
    ]
