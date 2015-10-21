# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0039_auto_20151016_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='company',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
