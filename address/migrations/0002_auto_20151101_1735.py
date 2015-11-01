# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='bank_account',
            field=models.CharField(max_length=255, null=True, verbose_name='bank account', blank=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='bank_code',
            field=models.CharField(max_length=255, null=True, verbose_name='bank code', blank=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='company_id',
            field=models.CharField(max_length=255, null=True, verbose_name='company ID', blank=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='company_name',
            field=models.CharField(max_length=255, null=True, verbose_name='company name', blank=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='vat_id',
            field=models.CharField(max_length=255, null=True, verbose_name='VAT ID', blank=True),
        ),
    ]
