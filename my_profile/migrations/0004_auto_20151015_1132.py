# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0003_my_profile_vz_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_profile',
            name='vz_id',
        ),
        migrations.AlterField(
            model_name='my_profile',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='my_profile',
            name='firstname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='my_profile',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='my_profile',
            name='pin_code',
            field=models.CharField(default=b'', max_length=6, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{6}$', message=b'Enter pin code.')]),
        ),
    ]
