# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_clothname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothname',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='clothname',
            name='pinyin',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tag',
            name='pinyin',
            field=models.CharField(max_length=40),
        ),
    ]
