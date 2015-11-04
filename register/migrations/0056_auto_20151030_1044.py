# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0055_auto_20151030_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'staticfiles'), null=True, upload_to=b'projectimg/', blank=True),
        ),
    ]
