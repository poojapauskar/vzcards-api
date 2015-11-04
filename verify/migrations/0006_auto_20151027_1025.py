# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0005_verify_access_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verify',
            old_name='access_token',
            new_name='token_generated',
        ),
    ]
