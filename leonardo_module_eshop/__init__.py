
from django.apps import AppConfig
from oscar import get_core_apps as get_eshop_apps
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'leonardo_module_eshop.EshopConfig'


try:
    # rename original oscar search
    from oscar.apps.search import config
    config.SearchConfig.label = 'oscar_search'
except Exception:
    pass


class OscarSearchConfig(AppConfig):
    name = 'oscar.apps.search'
    verbose_name = "oscar_search"


class Default(object):

    optgroup = ('Eshop')

    middlewares = [
        'oscar.apps.basket.middleware.BasketMiddleware',
    ]

    @property
    def apps(self):
        oscar_apps = get_eshop_apps()

        return [
            'leonardo_module_eshop',
            'oscarapi',
            'whoosh',
            'oscar.apps.customer',
            'oscar.apps.catalogue',
        ] + oscar_apps

    auth_backends = [
        'oscar.apps.customer.auth_backends.EmailBackend'
    ]

    context_processors = [
        #'oscar.apps.search.context_processors.search_form',
        'oscar.apps.promotions.context_processors.promotions',
        'oscar.apps.checkout.context_processors.checkout',
        'oscar.apps.customer.notifications.context_processors.notifications',
        'oscar.core.context_processors.metadata',
    ]

    plugins = [
        ('leonardo_module_eshop.apps.eshop', _('Eshop'), ),
        ('leonardo_module_eshop.apps.basket', _('Shopping Cart'), ),
        ('leonardo_module_eshop.apps.checkout', _('Eshop Checkout'), ),
        ('leonardo_module_eshop.apps.customer', _('Customers'), ),
        ('leonardo_module_eshop.apps.catalog', _('Eshop Catalog'),),
        ('leonardo_module_eshop.apps.api', _('Eshop API'), ),
    ]

    widgets = [
        QuickCartWidget
    ]

    config = {
        'OSCAR_INITIAL_ORDER_STATUS': ('Pending', _('Order Initial status')),
        'OSCAR_INITIAL_LINE_STATUS': ('123456789', _('Line Initial status')),
        'OSCAR_IMAGE_FOLDER': ('eshop', _('Eshop Image Directory')),
        'OSCAR_DELETE_IMAGE_FILES': (True, _('Delete Image Files')),
        'OSCAR_PROMOTION_FOLDER': ('promotions', _('Promotions Directory')),
    }


class EshopConfig(AppConfig, Default):
    name = 'leonardo_module_eshop'
    verbose_name = "Eshop"

default = Default()
