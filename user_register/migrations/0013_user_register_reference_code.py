# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0012_auto_20160702_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_register',
            name='reference_code',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
