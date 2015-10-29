# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0046_auto_20151027_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'projectimg/', blank=True),
        ),
    ]
