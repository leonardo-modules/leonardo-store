from oscar.apps.address.abstract_models import *  # noqa

from address.abstract_models import AbstractUserAddress

__all__ = []


class UserAddress(AbstractUserAddress):

    @property
    def salutation(self):
        """
        Name (including title)
        """
        if self.company_name and self.company_id and self.vat_id:
            return self.join_fields(
                ('company_name', 'company_id', 'vat_id'),
                separator=u"\n")
        return self.join_fields(
            ('title', 'first_name', 'last_name'),
            separator=u" ")

__all__.append('UserAddress')


from oscar.apps.address.models import *
