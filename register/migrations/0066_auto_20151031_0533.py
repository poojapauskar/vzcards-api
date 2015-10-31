# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0065_auto_20151030_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='photo',
            field=models.ImageField(default=b'projectimg/135762.jpg', null=True, upload_to=b'', blank=True),
        ),
    ]
