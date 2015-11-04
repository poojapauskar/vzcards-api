# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_create', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_create',
            name='item_photo',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
