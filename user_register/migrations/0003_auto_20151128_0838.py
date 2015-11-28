# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0002_auto_20151128_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='phone',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{12}$', message=b"Enter country code. Phone number must be entered in the format: '919999999'.")]),
        ),
    ]
