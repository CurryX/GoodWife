# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_auto_20180128_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_percent',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='picked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='washed',
            field=models.BooleanField(default=False),
        ),
    ]
