# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vzcards', models.CharField(default=b'https://vzcards-api.herokuapp.com/api/', max_length=100, blank=True)),
                ('register', models.CharField(default=b'https://vzcards-api.herokuapp.com/register/', max_length=100, blank=True)),
                ('verify', models.CharField(default=b'https://vzcards-api.herokuapp.com/verify/', max_length=100, blank=True)),
                ('create_object', models.CharField(default=b'https://vzcards-api.herokuapp.com/create_object/', max_length=100, blank=True)),
                ('connect', models.CharField(default=b'https://vzcards-api.herokuapp.com/connect/', max_length=100, blank=True)),
                ('get_list', models.CharField(default=b'https://vzcards-api.herokuapp.com/get_list/', max_length=100, blank=True)),
                ('get_my_tickets', models.CharField(default=b'https://vzcards-api.herokuapp.com/get_my_tickets/', max_length=100, blank=True)),
            ],
        ),
    ]
