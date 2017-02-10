# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_profile',
            name='address_line_1',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='address_line_2',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='city',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='email',
            field=models.EmailField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='firstname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='industry',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='lastname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='my_profile',
            name='pin_code',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
