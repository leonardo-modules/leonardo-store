from oscar.apps.order.abstract_models import *  # noqa
from oscar.core.loading import is_model_registered

from order.abstract_models import AbstractBillingAddress, AbstractShippingAddress

__all__ = ['PaymentEventQuantity', 'ShippingEventQuantity']


class BillingAddress(AbstractBillingAddress):
    pass

__all__.append('BillingAddress')


class ShippingAddress(AbstractShippingAddress):
    pass

__all__.append('ShippingAddress')


from oscar.apps.order.models import *
