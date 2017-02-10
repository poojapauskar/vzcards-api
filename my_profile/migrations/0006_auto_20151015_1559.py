# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0005_auto_20151015_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_profile',
            name='phone',
            field=models.CharField(default=b'', max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{12}$', message=b"Enter country code. Phone number must be entered in the format: '919999999'.")]),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='vz_id',
            field=models.CharField(default=b'', max_length=15, editable=False, blank=True),
        ),
    ]
