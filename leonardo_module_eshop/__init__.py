
from django.apps import AppConfig
from oscar import get_core_apps as get_eshop_apps
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'leonardo_module_eshop.EshopConfig'


class Default(object):

    optgroup = ('Eshop')

    #urls_conf = 'oscar.urls'

    @property
    def middlewares(self):
        return [
            'oscar.apps.basket.middleware.BasketMiddleware',
        ]

    @property
    def apps(self):
        return [
            'leonardo_module_eshop',
            'oscarapi',
            'whoosh',
            'oscar.apps.customer',
            'oscar.apps.catalogue',
        ] + get_eshop_apps()

    @property
    def auth_backends(self):
        return ['oscar.apps.customer.auth_backends.EmailBackend']

    @property
    def ctp(self):
        return [
            #'oscar.apps.search.context_processors.search_form',
            'oscar.apps.promotions.context_processors.promotions',
            'oscar.apps.checkout.context_processors.checkout',
            'oscar.apps.customer.notifications.context_processors.notifications',
            'oscar.core.context_processors.metadata',
        ]

    @property
    def plugins(self):
        return [
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

class EshopConfig(AppConfig, Default):
    name = 'leonardo_module_eshop'
    verbose_name = "Eshop"


default = Default()
