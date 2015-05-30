# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20150530_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='name', blank=True)),
            ],
            options={
                'verbose_name': 'product list',
                'verbose_name_plural': 'product lists',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductListItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='ordering')),
                ('extra_label', models.CharField(max_length=255, null=True, verbose_name='extra label', blank=True)),
                ('list', models.ForeignKey(verbose_name='list', to='leonardo_store.ProductList')),
                ('product', models.ForeignKey(verbose_name='product', to='catalogue.Product')),
            ],
            options={
                'verbose_name': 'product list item',
                'verbose_name_plural': 'product list items',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productlist',
            name='items',
            field=models.ManyToManyField(to='catalogue.Product', null=True, verbose_name='items', through='leonardo_store.ProductListItem', blank=True),
            preserve_default=True,
        ),
    ]
