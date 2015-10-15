# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0017_auto_20151014_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user_details',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default=b'424137', max_length=100, editable=False, blank=True),
        ),
    ]
