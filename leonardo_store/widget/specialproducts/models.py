
from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget

TYPE_CHOICES = (
    ('featured', _('featured')),
    ('new', _('new')),
    ('random', _('random')),
    ('is_discountable', _('is discountable ?')),
    ('rating', _('by rating')),
)


class SpecialProductsWidget(Widget):
    type = models.CharField(
        max_length=64, verbose_name=_("special"), choices=TYPE_CHOICES, default='featured')
    item_count = models.IntegerField(verbose_name=_("items to show"), default=12)
    random_order = models.BooleanField(
        verbose_name=_("show products in random order?"), default=False)

    @property
    def by_rating(self):
        """returns product by user rating
        """
        raise NotImplementedError

    @property
    def discountable(self):
        """returns discountable products
        """
        raise NotImplementedError

    class Meta:
        abstract = True
        verbose_name = _("special products")
        verbose_name_plural = _("special products")
