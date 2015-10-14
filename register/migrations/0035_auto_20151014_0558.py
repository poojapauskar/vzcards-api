# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0034_auto_20151013_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")]),
        ),
    ]
