from django.utils.translation import ugettext_lazy as _
from order.abstract_models import AbstractAddressExtension
from oscar.apps.address.abstract_models import AbstractUserAddress


class AbstractUserAddress(AbstractUserAddress, AbstractAddressExtension):
    """
    A user's address.  A user can have many of these and together they form an
    'address book' of sorts for the user.
    We use a separate model for shipping and billing (even though there will be
    some data duplication) because we don't want shipping/billing addresses
    changed or deleted once an order has been placed.  By having a separate
    model, we allow users the ability to add/edit/delete from their address
    book without affecting orders already placed.
    """
    class Meta:
        abstract = True
        app_label = 'address'
        verbose_name = _("User address")
        verbose_name_plural = _("User addresses")
        ordering = ['-num_orders']
        unique_together = ('user', 'hash')
