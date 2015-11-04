# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_image',
            name='link',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
