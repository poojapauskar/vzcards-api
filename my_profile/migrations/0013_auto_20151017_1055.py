# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0012_my_profile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_profile',
            name='email',
            field=models.EmailField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='my_profile',
            name='firstname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='my_profile',
            name='lastname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
