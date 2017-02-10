# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_ticket',
            name='access_token',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='create_ticket',
            name='vz_id',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
