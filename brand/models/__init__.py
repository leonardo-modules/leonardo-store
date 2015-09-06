from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms.translations import (TranslatedObjectManager,
                                  TranslatedObjectMixin, Translation)

from . import abstract_models


class Brand(abstract_models.AbstractBrand, TranslatedObjectMixin):

    objects = TranslatedObjectManager()


class BrandTranslation(Translation(Brand)):

    """
    Translated brand name and description.
    """

    name = models.CharField(_('name'), max_length=200)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        verbose_name = _('Translation')
        verbose_name_plural = _('Translations')

    def __unicode__(self):
        return self.name
