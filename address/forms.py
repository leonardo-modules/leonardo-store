from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from leonardo.forms import FormHelper, Accordion, Layout, AccordionGroup, Tab, Field
from oscar.core.loading import get_model
from oscar.views.generic import PhoneNumberMixin

UserAddress = get_model('address', 'useraddress')


class AbstractAddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        Set fields in OSCAR_REQUIRED_ADDRESS_FIELDS as required.
        """
        super(AbstractAddressForm, self).__init__(*args, **kwargs)
        field_names = (set(self.fields) &
                       set(settings.OSCAR_REQUIRED_ADDRESS_FIELDS))
        for field_name in field_names:
            self.fields[field_name].required = True

        # basic layout
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Accordion(
                AccordionGroup(_('Contact Information'),
                               'title', 'first_name', 'last_name',
                               'line1', 'line2', 'line3', 'line4',
                               'state', 'postcode', 'country',
                               'phone_number', 'notes'
                               ),
                AccordionGroup(_('Billing Information'),
                               'company_name', 'company_id',
                               'vat_id',
                               )
            )
        )


class UserAddressForm(PhoneNumberMixin, AbstractAddressForm):

    class Meta:
        model = UserAddress
        fields = [
            'title', 'first_name', 'last_name',
            'line1', 'line2', 'line3', 'line4',
            'company_name', 'company_id',
            'vat_id', 'state', 'postcode', 'country',
            'phone_number', 'notes',
        ]

    def __init__(self, user, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        self.instance.user = user
