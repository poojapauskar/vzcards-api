# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0053_remove_register_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'', blank=True),
        ),
    ]
