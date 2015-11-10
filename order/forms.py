
from django.utils.translation import ugettext_lazy as _
from leonardo.forms import (Accordion, AccordionGroup, Field, FormHelper,
                            Layout, Tab)
from oscar.apps.address.forms import AbstractAddressForm
from oscar.core.compat import get_user_model
from oscar.core.loading import get_model
from oscar.views.generic import PhoneNumberMixin

Country = get_model('address', 'Country')
BillingAddress = get_model('order', 'BillingAddress')
User = get_user_model()

ADDRESS_FIELDS = [
    'title', 'first_name', 'last_name',
    'line1', 'line2', 'line3', 'line4',
    'company_name', 'company_id', 'vat_id',
    'state', 'postcode', 'country',
    'phone_number', 'notes',
]


class ShippingAddressForm(PhoneNumberMixin, AbstractAddressForm):

    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        self.adjust_country_field()

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

    def adjust_country_field(self):
        countries = Country._default_manager.filter(
            is_shipping_country=True)

        # No need to show country dropdown if there is only one option
        if len(countries) == 1:
            self.fields.pop('country', None)
            self.instance.country = countries[0]
        else:
            self.fields['country'].queryset = countries
            self.fields['country'].empty_label = None

    class Meta:
        model = get_model('order', 'shippingaddress')
        fields = ADDRESS_FIELDS


class BillingAddressForm(PhoneNumberMixin, AbstractAddressForm):

    def __init__(self, *args, **kwargs):
        super(BillingAddressForm, self).__init__(*args, **kwargs)
        self.set_country_queryset()

    def set_country_queryset(self):
        self.fields['country'].queryset = Country._default_manager.all()

    class Meta:
        model = BillingAddress
        fields = ADDRESS_FIELDS
