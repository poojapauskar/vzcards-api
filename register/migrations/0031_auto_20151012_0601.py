# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0030_auto_20151012_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='vz_id',
            field=models.CharField(default=b'', max_length=15, null=True, editable=False, blank=True),
        ),
    ]
