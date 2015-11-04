# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0045_auto_20151027_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='access_token',
            new_name='token_generated',
        ),
    ]
