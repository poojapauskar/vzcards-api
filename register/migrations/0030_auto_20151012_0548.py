# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0029_auto_20151011_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='otp_generated',
            field=models.CharField(default=b'', max_length=100, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='vz_id',
            field=models.CharField(default=b'', max_length=15, editable=False, blank=True),
        ),
    ]
