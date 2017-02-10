# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('send_again', '0003_auto_20151128_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_again',
            name='phone',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{11,14}$', message=b"Enter country code. Phone number must be entered in the format: '+919999999'.")]),
        ),
    ]
