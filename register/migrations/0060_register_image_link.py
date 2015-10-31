# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0059_auto_20151030_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='image_link',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
