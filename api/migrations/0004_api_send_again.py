# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_api_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='send_again',
            field=models.CharField(default=b'https://vzcards-api.herokuapp.com/send_again/', max_length=100, blank=True),
        ),
    ]
