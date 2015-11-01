# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20151101_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='bank_account',
            field=models.CharField(max_length=255, null=True, verbose_name='bank account', blank=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='bank_code',
            field=models.CharField(max_length=255, null=True, verbose_name='bank code', blank=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='company_id',
            field=models.CharField(max_length=255, null=True, verbose_name='company ID', blank=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='company_name',
            field=models.CharField(max_length=255, null=True, verbose_name='company name', blank=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='vat_id',
            field=models.CharField(max_length=255, null=True, verbose_name='VAT ID', blank=True),
        ),
    ]
