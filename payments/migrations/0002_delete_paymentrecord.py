# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 08:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentRecord',
        ),
    ]