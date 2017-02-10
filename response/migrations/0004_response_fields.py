# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0003_remove_response_vz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='fields',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
