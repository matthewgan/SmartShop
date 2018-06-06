# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tag_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='EPC',
            field=models.CharField(max_length=24, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='TID',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
