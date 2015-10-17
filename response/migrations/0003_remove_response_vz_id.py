# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0002_response_vz_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='vz_id',
        ),
    ]
