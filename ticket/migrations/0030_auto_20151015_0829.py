# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0029_auto_20151015_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default=b'574044', max_length=100, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user_details',
            field=models.CharField(max_length=10000, editable=False, blank=True),
        ),
    ]
