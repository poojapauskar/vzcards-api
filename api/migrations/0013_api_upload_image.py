# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20151031_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='upload_image',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/upload_image/', max_length=100, blank=True),
        ),
    ]
