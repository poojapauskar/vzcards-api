# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0019_auto_20170123_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='is_organization',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
