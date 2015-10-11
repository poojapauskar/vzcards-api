# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_list', '0002_remove_get_list_date_validity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='get_list',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='get_list',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='get_list',
            name='description',
        ),
        migrations.RemoveField(
            model_name='get_list',
            name='item',
        ),
        migrations.RemoveField(
            model_name='get_list',
            name='question',
        ),
        migrations.RemoveField(
            model_name='get_list',
            name='vz_id',
        ),
    ]
