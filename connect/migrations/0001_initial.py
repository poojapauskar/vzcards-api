# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('connecter_vz_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('phone_1', models.CharField(default=b'', max_length=100, blank=True)),
                ('ticket_id_1', models.CharField(default=b'', max_length=100, blank=True)),
                ('phone_2', models.CharField(default=b'', max_length=100, blank=True)),
                ('ticket_id_2', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
    ]
