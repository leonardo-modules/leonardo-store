# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import oscar.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20150113_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='bank_account',
            field=models.CharField(max_length=255, null=True, verbose_name='bank account', blank=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='bank_code',
            field=models.CharField(max_length=255, null=True, verbose_name='bank code', blank=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='company_id',
            field=models.CharField(max_length=255, null=True, verbose_name='company ID', blank=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='company_name',
            field=models.CharField(max_length=255, null=True, verbose_name='company name', blank=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='notes',
            field=models.TextField(help_text='Tell us anything we should know when delivering your order.', verbose_name='Instructions', blank=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='phone_number',
            field=oscar.models.fields.PhoneNumberField(help_text='In case we need to call you about your order', verbose_name='Phone number', blank=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='vat_id',
            field=models.CharField(max_length=255, null=True, verbose_name='VAT ID', blank=True),
        ),
    ]
