# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-19 01:12
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=b''),
        ),
    ]