# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-19 01:13
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_work', '0002_auto_20170118_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media'), upload_to=b''),
        ),
    ]
