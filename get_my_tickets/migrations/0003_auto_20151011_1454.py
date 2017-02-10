# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_my_tickets', '0002_remove_get_my_tickets_date_validity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='get_my_tickets',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='get_my_tickets',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='get_my_tickets',
            name='description',
        ),
        migrations.RemoveField(
            model_name='get_my_tickets',
            name='item',
        ),
        migrations.RemoveField(
            model_name='get_my_tickets',
            name='question',
        ),
        migrations.RemoveField(
            model_name='get_my_tickets',
            name='vz_id',
        ),
    ]
