# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0035_auto_20151014_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{12}$', message=b"Enter country code. Phone number must be entered in the format: '919999999'.")]),
        ),
    ]
