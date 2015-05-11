
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'eshop_paypal.PaypalConfig'


class Default(object):

    apps = [
            'eshop_paypal',
            'paypal',
    ]

    plugins = [
        ('eshop_paypal.apps.paypal', _('Paypal'), ),
    ]

    config = {
        'PAYPAL_API_USERNAME': ('test_xxxx.gmail.com', _('Paypal API Username')),
        'PAYPAL_API_PASSWORD': ('123456789', _('Paypal API Password')),
        'PAYPAL_API_SIGNATURE': ('...', _('Paypal API Signature')),
    }


class PaypalConfig(AppConfig, Default):
    name = 'eshop_paypal'
    verbose_name = "Eshop Paypal"

default = Default()
