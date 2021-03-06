# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import faces.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baidu_appid', models.CharField(max_length=128)),
                ('baidu_group_id', models.CharField(max_length=128)),
                ('baidu_uid', models.CharField(max_length=128)),
                ('baidu_faceid', models.CharField(max_length=128)),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=faces.models.scramble_uploaded_filename, verbose_name='Uploaded image')),
                ('filename', models.CharField(blank=True, max_length=100)),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.Customer')),
            ],
        ),
    ]
