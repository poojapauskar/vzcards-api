# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0036_auto_20151014_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='address_line_1',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='register',
            name='address_line_2',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='register',
            name='city',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='register',
            name='industry',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='register',
            name='pin_code',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
