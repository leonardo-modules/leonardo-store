
'''

Simple Plugable Payment Methods for Django Oscar

inspired from shipping method

Inherit from ``PaymentMethod`` and define your Payment Method details.::

    class DummyPaymentMethod(PaymentMethod):

        code = 'dummy'
        name = _('Dummy')
        description = _('Dummy Payment Gateway')

        view = ExampleView


call ``override_checkout`` from ``leonardo_store.payments.utils``

Thats all, your Payment Method will be available in payment method view

'''

from .methods import PaymentMethod
from .repository import Repository

from .utils import override_checkout

__all__ = ('PaymentMethod', 'override_checkout', 'Repository')
