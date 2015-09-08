
from django.utils.translation import ugettext_lazy as _
from django import forms

ORDER_BY_CHOICES = (
    ('price', _('Price asc')),
    ('-price', _('Price desc')),
    ('availability', _('Availability')),
)


class OrderByForm(forms.Form):

    order_by = forms.ChoiceField(
        label=_('Order By'),
        choices=ORDER_BY_CHOICES,
        required=False)
