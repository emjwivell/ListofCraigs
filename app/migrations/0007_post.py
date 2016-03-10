# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160310_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory')),
            ],
            options={
                'ordering': ['-time_created'],
            },
        ),
    ]