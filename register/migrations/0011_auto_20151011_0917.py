# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20151011_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='otp_generated',
            field=models.CharField(default=b'459189', max_length=100, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='vz_id',
            field=models.CharField(default=b'VZ1444555079.09', max_length=15, editable=False),
        ),
    ]
