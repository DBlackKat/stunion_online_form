# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reflect', '0009_auto_20170201_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.BooleanField(default=False)),
                ('reflection', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='reflect.Reflection')),
            ],
        ),
        migrations.RemoveField(
            model_name='firstvisit',
            name='reflection',
        ),
        migrations.DeleteModel(
            name='FirstVisit',
        ),
    ]
