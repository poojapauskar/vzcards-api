# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0003_remove_verify_vz_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verify',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{12}$', message=b"Enter country code. Phone number must be entered in the format: '+919999999'.")]),
        ),
    ]
