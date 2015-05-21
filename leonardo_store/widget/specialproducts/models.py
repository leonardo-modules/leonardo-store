# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from webcms.models import Widget

TYPE_CHOICES = (
    ('featured', 'featured'),
    ('new', 'new'),
    ('random', 'random'),
)

class SpecialProductsWidget(Widget):
    type = models.CharField(max_length=64, verbose_name=_("special"), choices=TYPE_CHOICES, default='featured')
    item_count = models.IntegerField(verbose_name=_("items to show"), default=12)
    random_order = models.BooleanField(verbose_name=_("show products in random order?"), default=False)

    class Meta:
        abstract = True
        verbose_name = _("special products")
        verbose_name_plural = _("special products")
