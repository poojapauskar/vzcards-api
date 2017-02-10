# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0011_user_register_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='pin_code',
            field=models.CharField(default=b'', max_length=6, blank=True),
        ),
    ]
