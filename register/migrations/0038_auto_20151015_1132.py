# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0037_auto_20151015_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pin_code',
            field=models.CharField(default=b'', max_length=6, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{6}$', message=b'Enter pin code.')]),
        ),
    ]
