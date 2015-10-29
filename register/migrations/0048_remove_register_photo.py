# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0047_register_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='photo',
        ),
    ]
