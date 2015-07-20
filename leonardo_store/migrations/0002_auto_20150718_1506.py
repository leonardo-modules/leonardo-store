# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='items',
            field=models.ManyToManyField(to='catalogue.Product', verbose_name='items', through='leonardo_store.ProductListItem', blank=True),
            preserve_default=True,
        ),
    ]
