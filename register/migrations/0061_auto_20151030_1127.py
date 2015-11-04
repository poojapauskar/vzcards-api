# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0060_register_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='image_link',
        ),
        migrations.AlterField(
            model_name='register',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
