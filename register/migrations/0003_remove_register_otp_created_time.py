# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-08 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_register_otp_created_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='otp_created_time',
        ),
    ]