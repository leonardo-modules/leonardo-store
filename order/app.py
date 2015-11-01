from django.utils.translation import ugettext_lazy as _
from oscar.apps.order.config import OrderConfig


class Config(OrderConfig):
    label = 'order'
    name = 'order'
    verbose_name = _('Order')

    def ready(self):
        from .forms import BillingAddressForm, ShippingAddressForm
        from oscar.apps.payment import forms
        from oscar.apps.checkout import forms as checkout_forms
        from oscar.apps.checkout import views
        from oscar.apps.checkout.app import application
        forms.BillingAddressForm = BillingAddressForm
        checkout_forms.ShippingAddressForm = ShippingAddressForm
        views.ShippingAddressForm = ShippingAddressForm
        views.ShippingAddressView.form_class = ShippingAddressForm
        application.shipping_address_view = views.ShippingAddressView
        from oscar.apps.dashboard.orders import views as dashboard_views
        dashboard_views.ShippingAddressForm = ShippingAddressForm
        dashboard_views.ShippingAddressUpdateView.form_class = ShippingAddressForm
