# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(default='wxff1e7b77ac356972', max_length=20)),
                ('mch_id', models.CharField(default='1484700102', max_length=12)),
                ('sub_mch_id', models.CharField(default='1505139251', max_length=12)),
                ('sub_app_id', models.CharField(default='wx18902f96ec8fb847', max_length=20)),
                ('sub_open_id', models.CharField(max_length=30)),
                ('body', models.CharField(default='物掌柜智慧便利', max_length=200)),
                ('nonce_str', models.CharField(default='4481528965', max_length=10)),
                ('notify_url', models.CharField(default='https://www.wuzhanggui.shop/api/payment/wechatnotify/', max_length=200)),
                ('out_trade_no', models.CharField(max_length=20)),
                ('spbill_create_ip', models.CharField(default='192.168.123.97', max_length=20)),
                ('total_fee', models.CharField(max_length=20)),
                ('trade_type', models.CharField(max_length=10)),
                ('sign', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('prepay_sign', models.CharField(blank=True, max_length=100)),
                ('prepay_id', models.CharField(blank=True, max_length=100)),
                ('pay_sign', models.CharField(blank=True, max_length=100)),
                ('query_sign', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
