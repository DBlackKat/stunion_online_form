# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reflect', '0011_auto_20170201_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='reflection',
        ),
        migrations.AddField(
            model_name='reflection',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
