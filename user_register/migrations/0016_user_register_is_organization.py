# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0015_remove_user_register_is_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_register',
            name='is_organization',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
