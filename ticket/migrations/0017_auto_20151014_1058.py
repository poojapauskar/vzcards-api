# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0016_auto_20151014_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user_details',
            field=models.CharField(max_length=200, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default=b'226747', max_length=100, editable=False, blank=True),
        ),
    ]
