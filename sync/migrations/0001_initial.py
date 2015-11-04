# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import sync.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vz_id', models.CharField(default=b'', max_length=255, blank=True)),
                ('contact_list', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=b'', blank=True), size=None)),
                ('friends_vz_id', sync.models.ListField(default=b'', editable=False, blank=True)),
            ],
        ),
    ]
