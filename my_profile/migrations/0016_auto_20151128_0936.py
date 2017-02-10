# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0015_auto_20151031_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_profile',
            name='phone',
            field=models.CharField(default=b'', max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{11,13}$', message=b"Enter country code. Phone number must be entered in the format: '919999999'.")]),
        ),
    ]
