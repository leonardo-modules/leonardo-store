# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oscar.models.fields.autoslugfield
import brand.models.fields
import feincms.translations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', oscar.models.fields.autoslugfield.AutoSlugField(populate_from=b'name', editable=False, max_length=100, blank=True, unique=True, verbose_name='Slug')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('formula', brand.models.fields.FormulaField(max_length=100, null=True, verbose_name='Formula', blank=True)),
                ('country', models.ForeignKey(verbose_name='Country', to='address.Country')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='BrandTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'en', max_length=10, verbose_name='language', choices=[(b'en', b'EN'), (b'cs', b'CS')])),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('parent', models.ForeignKey(related_name='translations', to='brand.Brand')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
    ]
