# -#- coding: utf-8 -#-

from django import forms

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext, loader

from webcms.models import Widget

from satchmo_ext.brand.models import Brand
from product.models import Category

from django.conf import settings

if 'webcms.module.store.ext.manufacturer' in settings.INSTALLED_APPS:
    SHOW_CHOICES = (
        ('category', _("categories only")),
        ('brand', _("brands only")),
        ('manuf', _("manufacturers only")),
        ('all', _("Categories and brands")),
        ('all_manuf', _("Categories and manufacturers")),
    )
else:
    SHOW_CHOICES = (
        ('category', _("categories only")),
        ('brand', _("brands only")),
        ('all', _("both categories and brands")),
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

        if 'webcms.module.store.ext.manufacturer' in settings.INSTALLED_APPS:
            from webcms.module.store.ext.manufacturer.models import Manufacturer
            try:
                manufacturer_current = Manufacturer.objects.get(pk=request._feincms_fragments["current_manufacturer"].strip())
            except:
                manufacturer_current = None
        else:
            manufacturer_current = None

        try:
            category_current = Category.objects.get(pk=request._feincms_fragments["current_category"].strip())
        except:
            category_current = None

        try:
            brand_current = Brand.objects.get(pk=request._feincms_fragments["current_brand"].strip())
        except:
            brand_current = None

        if self.list == 'all' or self.list == 'category':
            brand_list = Brand.objects.active()
        else:
            brand_list = None

        if self.list == 'all' or self.list == 'brand':
            brand_list = Brand.objects.active()
        else:
            brand_list = None

        category_list = Category.objects.filter(parent__isnull=True, is_active=True)

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

        if 'webcms.module.store.ext.manufacturer' in settings.INSTALLED_APPS:
            from webcms.module.store.ext.manufacturer.models import Manufacturer
            manufacturer_list = Manufacturer.objects.active()
        else:
            manufacturer_list = []

        template = loader.get_template(self.template_name)
        context = RequestContext(options['request'], {
            'widget': self,
            'request': request,
            'category_current': category_current,
            'category_list': category_list,
            'brand_current': brand_current,
            'brand_list': brand_list,
            'manufacturer_current': manufacturer_current,
            'manufacturer_list': manufacturer_list,
            'level_0': level_0,
            'level_1': level_1,
            'level_2': level_2,
            'level_3': level_3,
        })
        return template.render(context)

    class Meta:
        abstract = True
        verbose_name = _("product catalog")
        verbose_name_plural = _("product catalogs")
