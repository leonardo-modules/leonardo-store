
from django.apps import AppConfig
from oscar import get_core_apps as get_eshop_apps
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'leonardo_store.Config'


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

    optgroup = ('Store')

    middlewares = [
        'oscar.apps.basket.middleware.BasketMiddleware',
    ]

    @property
    def apps(self):
        oscar_apps = get_eshop_apps()

        return [
            'leonardo_store',
            'oscarapi',
            'whoosh',
            'oscar.apps.customer',
            'oscar.apps.catalogue',
        ] + oscar_apps

    auth_backends = [
        'oscar.apps.customer.auth_backends.EmailBackend'
    ]

    context_processors = [
        'oscar.apps.promotions.context_processors.promotions',
        'oscar.apps.checkout.context_processors.checkout',
        'oscar.apps.customer.notifications.context_processors.notifications',
        'oscar.core.context_processors.metadata',
    ]

    plugins = [
        ('leonardo_store.apps.eshop', _('Store'), ),
        ('leonardo_store.apps.basket', _('Shopping Cart'), ),
        ('leonardo_store.apps.checkout', _('Store Checkout'), ),
        ('leonardo_store.apps.customer', _('Customers'), ),
        ('leonardo_store.apps.catalog', _('Store Catalog'),),
        ('leonardo_store.apps.api', _('Store API'), ),
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

    absolute_url_overrides = {
        'catalogue.product': 'leonardo_store.overrides.oscar_product_url_app',
        'catalogue.category': 'leonardo_store.overrides.category',
    }

    navigation_extensions = [
        'leonardo_store.navigation_extensions.categories'
    ]


class Config(AppConfig, Default):
    name = 'leonardo_store'
    verbose_name = "Store"

default = Default()
