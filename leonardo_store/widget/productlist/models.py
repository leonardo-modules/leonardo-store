# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget
from leonardo_store.models import ProductList


class ProductListWidget(Widget):
    list = models.ForeignKey(ProductList, verbose_name=_("product list"))
    pagination = models.IntegerField(verbose_name=_("items per page"), default=12)
    random_order = models.BooleanField(verbose_name=_("show products in random order?"), default=False)

    class Meta:
        abstract = True
        verbose_name = _("product list")
        verbose_name_plural = _("product lists")
