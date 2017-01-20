# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0016_user_register_is_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='reference_code',
            field=models.CharField(default=1, max_length=100, blank=True),
        ),
    ]
