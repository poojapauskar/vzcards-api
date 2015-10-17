# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0040_register_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='firstname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='lastname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
