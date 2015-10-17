# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='contacts',
            new_name='friends_vz_id',
        ),
    ]
