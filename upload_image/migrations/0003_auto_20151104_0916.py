# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_image', '0002_upload_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_image',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'/projectimg', blank=True),
        ),
    ]
