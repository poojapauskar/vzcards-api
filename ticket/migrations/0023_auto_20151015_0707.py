# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0022_auto_20151015_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default=b'118064', max_length=100, editable=False, blank=True),
        ),
    ]
