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

        manufacturer_list = Partner.objects.all()

        context = RequestContext(options['request'], {
            'widget': self,
            'request': request,
            'manufacturer_list': manufacturer_list,
        })
        return render_to_string(self.get_template, context)

    class Meta:
        abstract = True
        verbose_name = _("Product catalog")
        verbose_name_plural = _("Product catalogs")
