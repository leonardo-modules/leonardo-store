# -#- coding: utf-8 -#-

from django import forms

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext, loader

from django.template.loader import render_to_string

from leonardo.module.web.models import Widget

from oscar.core.loading import get_class

from django.conf import settings

SHOW_CHOICES = (
    ('category', _("categories only")),
    ('manuf', _("manufacturers only")),
    ('all_manuf', _("Categories and manufacturers")),
)


def get_parent_category(category):
    if category.parent:
        return category.parent
    else:
        return False


class ProductCatalogWidget(Widget):
    list = models.CharField(max_length=255, verbose_name=_("list"), choices=SHOW_CHOICES, default="category")
    show_product_count = models.BooleanField(verbose_name=_("show product count"), default=False)

    def render_content(self, options):
        request = options['request']

        Partner = get_class('partner.models', 'Partner')

        try:
            manufacturer_current = Partner.objects.get(pk=request._feincms_fragments["current_manufacturer"].strip())
        except:
            manufacturer_current = None

        try:
            category_current = Category.objects.get(pk=request._feincms_fragments["current_category"].strip())
        except:
            category_current = None

        Category = get_class('catalogue.categories', 'Category')
        category_list = Category.objects.filter(depth=1)

        path_to_root = []
        if category_current:
            category = category_current
            while category:
                path_to_root.append(category)
                category = get_parent_category(category)
            path_to_root.reverse()
            level_0 = path_to_root[0]
        else:
            level_0 = False
        if len(path_to_root) > 0:
            level_1 = path_to_root[0]
        else:
            level_1 = False
        if len(path_to_root) > 1:
            level_2 = path_to_root[1]
        else:
            level_2 = False
        if len(path_to_root) > 2:
            level_3 = path_to_root[2]
        else:
            level_3 = False
        if len(path_to_root) > 3:
            level_4 = path_to_root[3]
        else:
            level_4 = False
        if len(path_to_root) > 4:
            level_5 = path_to_root[4]
        else:
            level_5 = False
        if len(path_to_root) > 5:
            level_6 = path_to_root[5]
        else:
            level_6 = False

        manufacturer_list = Partner.objects.all()

        context = RequestContext(options['request'], {
            'widget': self,
            'request': request,
            'category_current': category_current,
            'category_list': category_list,
            'manufacturer_current': manufacturer_current,
            'manufacturer_list': manufacturer_list,
            'level_0': level_0,
            'level_1': level_1,
            'level_2': level_2,
            'level_3': level_3,
        })
        return render_to_string(self.get_template, context)

    class Meta:
        abstract = True
        verbose_name = _("product catalog")
        verbose_name_plural = _("product catalogs")
