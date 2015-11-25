
from oscar.apps.catalogue.config import CatalogueConfig as OscarCatalogueConfig
from django.utils.translation import ugettext_lazy as _


class CatalogueConfig(OscarCatalogueConfig):
    label = 'catalogue'
    name = 'catalogue'
    verbose_name = _('Catalogue')

    def ready(self):
        super(CatalogueConfig, self).ready()
        from .utils import override_basket_tags
        override_basket_tags()
