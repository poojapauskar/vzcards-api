# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0007_auto_20151102_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='my_ticket',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='connect',
            name='reffered_phone',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{12}$', message=b"Enter country code. Phone number must be entered in the format: '919999999'.")]),
        ),
        migrations.AddField(
            model_name='connect',
            name='reffered_ticket',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
