# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0014_user_register_is_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_register',
            name='is_organization',
        ),
    ]
