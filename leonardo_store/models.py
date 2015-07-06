
from django.db import models

from django.utils.translation import ugettext_lazy as _


class ProductList(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"), blank=True, null=True)
    items = models.ManyToManyField(
        'catalogue.Product', verbose_name=_("items"), blank=True, through='ProductListItem')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('product list')
        verbose_name_plural = _('product lists')


class ProductListItem(models.Model):
    list = models.ForeignKey(ProductList, verbose_name=_("list"))
    product = models.ForeignKey('catalogue.Product', verbose_name=_("product"))
    ordering = models.PositiveIntegerField(verbose_name=_("ordering"), default=0)
    extra_label = models.CharField(
        max_length=255, verbose_name=_("extra label"), blank=True, null=True)

    def __unicode__(self):
        return u'%s: %s' % (self.list.name, self.product.slug)

    class Meta:
        verbose_name = _('product list item')
        verbose_name_plural = _('product list items')
