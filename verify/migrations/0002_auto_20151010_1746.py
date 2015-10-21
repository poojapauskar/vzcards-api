# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verify',
            name='vz_id',
            field=models.CharField(default=b'', max_length=100, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='verify',
            name='valid',
            field=models.CharField(default=b'', max_length=2, editable=False, blank=True),
        ),
    ]
