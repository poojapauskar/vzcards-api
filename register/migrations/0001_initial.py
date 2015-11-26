# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(default=b'', max_length=100, blank=True)),
                ('lastname', models.CharField(default=b'', max_length=100, blank=True)),
                ('email', models.EmailField(default=b'', max_length=100, blank=True)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{12}$', message=b"Enter country code. Phone number must be entered in the format: '919999999'.")])),
                ('vz_id', models.CharField(default=b'', max_length=15, blank=True)),
                ('otp_generated', models.CharField(default=b'', max_length=15, editable=False, blank=True)),
                ('industry', models.CharField(default=b'', max_length=100, blank=True)),
                ('company', models.CharField(default=b'', max_length=100, blank=True)),
                ('address_line_1', models.CharField(default=b'', max_length=100, blank=True)),
                ('address_line_2', models.CharField(default=b'', max_length=100, blank=True)),
                ('city', models.CharField(default=b'', max_length=100, blank=True)),
                ('pin_code', models.CharField(default=b'', max_length=6, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{6}$', message=b'Enter pin code.')])),
                ('token_generated', models.TextField(default=b'', blank=True)),
                ('photo', models.TextField(default=b'', blank=True)),
                ('company_photo', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
