# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0044_register_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='access_token',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
