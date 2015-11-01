from django.utils.translation import ugettext_lazy as _
from oscar.apps.address.config import AddressConfig


class Config(AddressConfig):
    label = 'address'
    name = 'address'
    verbose_name = _('Address')

    def ready(self):

        from .utils import override_address
        override_address()
