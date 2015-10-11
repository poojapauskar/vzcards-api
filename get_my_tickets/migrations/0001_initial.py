# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Get_my_tickets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('vz_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('question', models.CharField(default=b'', max_length=100, blank=True)),
                ('item', models.CharField(default=b'', max_length=100, blank=True)),
                ('description', models.TextField()),
                ('cost', models.CharField(default=b'', max_length=100, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_validity', models.CharField(default=b'', max_length=100, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
