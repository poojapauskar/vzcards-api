# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0052_auto_20151016_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='cost',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default=b'320011', max_length=100, editable=False, blank=True),
        ),
    ]
