
from django import forms
from django.conf import settings
from django.db.models import Sum
from django.forms.models import BaseModelFormSet, modelformset_factory
from django.utils.translation import ugettext_lazy as _

from oscar.core.loading import get_model
from oscar.forms import widgets
from oscar.apps.basket.forms import AddToBasketForm as OscarAddToBasketForm

Line = get_model('basket', 'line')
Basket = get_model('basket', 'basket')
Product = get_model('catalogue', 'product')


class AddToBasketForm(OscarAddToBasketForm):

    def _add_option_field(self, product, option):
        """
        Creates the appropriate form field for the product option.
        This is designed to be overridden so that specific widgets can be used
        for certain types of options.
        """
        self.fields[option.code] = option.formfield()

    def clean(self):
        info = self.basket.strategy.fetch_for_product(self.product)

        # Check currencies are sensible
        if (self.basket.currency and
                info.price.currency != self.basket.currency):
            raise forms.ValidationError(
                _("This product cannot be added to the basket as its currency "
                  "isn't the same as other products in your basket"))

        # Check user has permission to add the desired quantity to their
        # basket.
        current_qty = self.basket.product_quantity(self.product)
        desired_qty = current_qty + self.cleaned_data.get('quantity', 1)
        is_permitted, reason = info.availability.is_purchase_permitted(
            desired_qty)
        if not is_permitted:
            raise forms.ValidationError(reason)

        return self.cleaned_data

    # Helpers

    def cleaned_options(self):
        """
        Return submitted options in a clean format
        """
        options = []
        for option in self.parent_product.options:
            if option.code in self.cleaned_data and option.clean():
                options.append({
                    'option': option,
                    'value': self.cleaned_data[option.code]})
        return options


class SimpleAddToBasketForm(AddToBasketForm):
    """
    Simplified version of the add to basket form where the quantity is
    defaulted to 1 and rendered in a hidden widget
    """
    quantity = forms.IntegerField(
        initial=1, min_value=1, widget=forms.HiddenInput, label=_('Quantity'))
