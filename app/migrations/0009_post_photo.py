# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160310_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]