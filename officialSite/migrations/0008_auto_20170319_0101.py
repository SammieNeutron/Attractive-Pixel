# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officialSite', '0007_auto_20170319_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_showcase',
            name='modal_photos',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='client_showcase',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='modal_photos',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
