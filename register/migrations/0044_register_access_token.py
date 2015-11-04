# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0043_remove_register_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='access_token',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
