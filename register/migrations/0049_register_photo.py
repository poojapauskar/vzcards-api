# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0048_remove_register_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'projectimg/', blank=True),
        ),
    ]
