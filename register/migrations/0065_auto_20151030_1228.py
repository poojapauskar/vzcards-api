# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0064_auto_20151030_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
