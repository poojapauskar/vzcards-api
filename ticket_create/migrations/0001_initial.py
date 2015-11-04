# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket_create',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('vz_id', models.CharField(max_length=100)),
                ('user_details', models.TextField(default=b'', blank=True)),
                ('question', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_validity', models.DateField()),
                ('ticket_id', models.CharField(default=b'', max_length=100, editable=False, blank=True)),
                ('item_photo', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
